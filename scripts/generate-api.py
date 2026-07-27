"""
generate_api.py
───────────────
Walks the Lexigram monorepo, parses every public-API __init__.py, resolves
each exported symbol to its definition, and writes an api.md file into the
matching Starlight content directory.

Run:
    python docs/scripts/generate_api.py

Override the framework root for CI/CD:
    LEX_ROOT=/path/to/lexigram python docs/scripts/generate_api.py
"""

import ast
import os
import re
import textwrap
from pathlib import Path


# ── Paths ────────────────────────────────────────────────────────────────────

DOCS_ROOT      = Path(__file__).parent.parent
FRAMEWORK_ROOT = Path(os.environ.get("LEX_ROOT", str(DOCS_ROOT.parent / "lexigram")))
CONTENT_ROOT   = DOCS_ROOT / "src/content/docs"


# ── AST helpers ──────────────────────────────────────────────────────────────

# Proprietary / never-published packages — excluded from docs generation.
_PROPRIETARY_PKGS: frozenset = frozenset({
    "lexigram-ai-guard", "lexigram-ai-governance",
    "lexigram-ai-evaluation", "lexigram-ai-prompt",
})

#: Module-level AST cache — avoids re-parsing the same file twice.
_AST_CACHE: dict[str, ast.Module] = {}


def _parse_ast(file_path: Path) -> ast.Module | None:
    """Return a cached AST for *file_path*, or ``None`` on failure."""
    if not file_path.exists():
        return None
    key = str(file_path)
    if key not in _AST_CACHE:
        try:
            _AST_CACHE[key] = ast.parse(file_path.read_text())
        except Exception:
            return None
    return _AST_CACHE[key]


def _unparse_annotation(node) -> str:
    """Convert an AST annotation node to a human-readable type string."""
    if node is None:
        return ""
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_unparse_annotation(node.value)}.{node.attr}"
    if isinstance(node, ast.Subscript):
        return f"{_unparse_annotation(node.value)}[{_unparse_annotation(node.slice)}]"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return f"{_unparse_annotation(node.left)} | {_unparse_annotation(node.right)}"
    if isinstance(node, ast.Tuple):
        return ", ".join(_unparse_annotation(e) for e in node.elts)
    if isinstance(node, ast.List):
        return f"[{', '.join(_unparse_annotation(e) for e in node.elts)}]"
    if isinstance(node, ast.Index):        # Python < 3.9
        return _unparse_annotation(node.value)  # type: ignore[attr-defined]
    try:
        return ast.unparse(node)
    except Exception:
        return "..."


def _build_full_signature(func_node, *, skip_self: bool = True) -> str:
    """Return a full typed signature string from a function AST node.

    Includes parameter types, default values, ``*args``, ``**kwargs``, and
    the return annotation.
    """
    args        = func_node.args
    defaults    = args.defaults
    n_args      = len(args.args)
    n_defaults  = len(defaults)
    parts: list[str] = []

    for i, arg in enumerate(args.args):
        if skip_self and arg.arg == "self":
            continue
        ann     = _unparse_annotation(arg.annotation) if arg.annotation else ""
        di      = i - (n_args - n_defaults)           # index into defaults
        default = defaults[di] if di >= 0 else None

        if ann and default is not None:
            try:
                parts.append(f"{arg.arg}: {ann} = {ast.unparse(default)}")
            except Exception:
                parts.append(f"{arg.arg}: {ann}")
        elif ann:
            parts.append(f"{arg.arg}: {ann}")
        elif default is not None:
            try:
                parts.append(f"{arg.arg}={ast.unparse(default)}")
            except Exception:
                parts.append(arg.arg)
        else:
            parts.append(arg.arg)

    # *args or bare *
    if args.vararg:
        ann = _unparse_annotation(args.vararg.annotation) if args.vararg.annotation else ""
        parts.append(f"*{args.vararg.arg}: {ann}" if ann else f"*{args.vararg.arg}")
    elif args.kwonlyargs:
        parts.append("*")

    # keyword-only args
    for i, arg in enumerate(args.kwonlyargs):
        ann     = _unparse_annotation(arg.annotation) if arg.annotation else ""
        default = args.kw_defaults[i] if i < len(args.kw_defaults) else None
        if ann and default is not None:
            try:
                parts.append(f"{arg.arg}: {ann} = {ast.unparse(default)}")
            except Exception:
                parts.append(f"{arg.arg}: {ann}")
        elif ann:
            parts.append(f"{arg.arg}: {ann}")
        else:
            parts.append(arg.arg)

    # **kwargs
    if args.kwarg:
        ann = _unparse_annotation(args.kwarg.annotation) if args.kwarg.annotation else ""
        parts.append(f"**{args.kwarg.arg}: {ann}" if ann else f"**{args.kwarg.arg}")

    ret     = _unparse_annotation(func_node.returns) if func_node.returns else ""
    ret_str = f" -> {ret}" if ret else ""
    return f"({', '.join(parts)}){ret_str}"


def _get_param_types(func_node) -> dict[str, str]:
    """Extract parameter and return annotations into a ``{name: type_str}`` dict."""
    types: dict[str, str] = {}
    if not hasattr(func_node, "args"):
        return types

    args = func_node.args
    for arg in args.args + args.kwonlyargs:
        if arg.arg == "self":
            continue
        if arg.annotation:
            types[arg.arg] = _unparse_annotation(arg.annotation)

    if args.vararg and args.vararg.annotation:
        types[args.vararg.arg] = _unparse_annotation(args.vararg.annotation)
    if args.kwarg and args.kwarg.annotation:
        types[args.kwarg.arg] = _unparse_annotation(args.kwarg.annotation)
    if getattr(func_node, "returns", None):
        types["__return__"] = _unparse_annotation(func_node.returns)

    return types


# ── Module resolution ─────────────────────────────────────────────────────────

def _resolve_module_path(module_path: str) -> tuple[Path | None, Path | None]:
    """Locate a Python source file for *module_path* inside the monorepo.

    Returns ``(pkg_root, file_path)`` or ``(None, None)`` when not found.
    """
    parts        = module_path.split(".")
    rel_py       = "/".join(parts) + ".py"
    rel_init     = "/".join(parts) + "/__init__.py"

    print(f"      [?] Resolving {module_path}")

    for pkg_dir in FRAMEWORK_ROOT.iterdir():
        if not pkg_dir.is_dir():
            continue
        src = pkg_dir / "src"
        if not src.exists():
            continue
        for rel in (rel_py, rel_init):
            candidate = src / rel
            if candidate.exists():
                return pkg_dir, candidate

    return None, None


def _find_definition(module_path: str, name: str, visited: set | None = None) -> dict | None:
    """Recursively locate the definition of *name* starting from *module_path*.

    Follows import aliases and re-exports transparently.  Returns a rich dict
    describing the symbol, or ``None`` when the symbol cannot be resolved.
    """
    if visited is None:
        visited = set()
    key = (module_path, name)
    if key in visited:
        return None
    visited.add(key)

    print(f"    [D] find_definition({module_path}, {name})")

    _, file_path = _resolve_module_path(module_path)
    if not file_path:
        print(f"      [!] Could not resolve path for {module_path}")
        return None

    print(f"      [V] Resolved to {file_path}")
    tree = _parse_ast(file_path)
    if not tree:
        return None

    # ── 1. Direct class / function definition ──────────────────────────────
    for node in tree.body:
        if not (
            isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == name
        ):
            continue

        is_class = isinstance(node, ast.ClassDef)
        is_async = isinstance(node, ast.AsyncFunctionDef)
        docstring = ast.get_docstring(node) or ""
        signature = ""
        methods: list[dict] = []
        param_types: dict[str, str] = {}
        lineno     = node.lineno

        try:
            repo_path = file_path.relative_to(FRAMEWORK_ROOT).as_posix()
        except Exception:
            repo_path = ""

        if not is_class:
            signature   = _build_full_signature(node)
            param_types = _get_param_types(node)
        else:
            for child in node.body:
                if not isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if child.name.startswith("_") and child.name != "__init__":
                    continue
                c_async = isinstance(child, ast.AsyncFunctionDef)
                c_prop  = any(
                    isinstance(d, ast.Name) and d.id == "property"
                    for d in getattr(child, "decorator_list", [])
                )
                m_gh = f"https://github.com/dbtinoy-/lexigram/blob/main/{repo_path}#L{child.lineno}" if repo_path else ""
                methods.append({
                    "name":        child.name,
                    "signature":   _build_full_signature(child),
                    "docstring":   ast.get_docstring(child) or "",
                    "is_async":    c_async,
                    "is_property": c_prop,
                    "param_types": _get_param_types(child),
                    "lineno":      child.lineno,
                    "github_url":  m_gh,
                })

        # Determine symbol group
        group = "Functions"
        if is_class:
            bases = [
                getattr(b, "id", "")
                for b in node.bases
                if isinstance(b, ast.Name)
            ]
            if any(
                b.endswith("Error") or b in ("Exception", "BaseException", "LexigramError", "AIError")
                for b in bases
            ):
                group = "Exceptions"
            elif any(b == "Protocol" for b in bases):
                group = "Protocols"
            else:
                group = "Classes"

        gh_url = f"https://github.com/dbtinoy-/lexigram/blob/main/{repo_path}#L{lineno}" if repo_path else ""

        return {
            "docstring":   docstring,
            "signature":   signature,
            "param_types": param_types,
            "lineno":      lineno,
            "github_url":  gh_url,
            "repo_path":   repo_path,
            "is_class":    is_class,
            "is_async":    is_async,
            "group":       group,
            "methods":     methods,
        }

    # ── 2. Assignment alias ────────────────────────────────────────────────
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    if isinstance(node.value, ast.Name):
                        return _find_definition(module_path, node.value.id, visited)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                if isinstance(node.value, ast.Name):
                    return _find_definition(module_path, node.value.id, visited)

    # ── 3. Import re-export ────────────────────────────────────────────────
    for node in tree.body:
        if not isinstance(node, ast.ImportFrom):
            continue
        for alias in node.names:
            exported_as = alias.asname or alias.name
            if exported_as != name:
                continue
            target_module = node.module or ""
            if node.level > 0:
                base = module_path.split(".")[: -node.level]
                target_module = ".".join(base + ([target_module] if target_module else []))
            if target_module:
                return _find_definition(target_module, alias.name, visited)

    return None


# ── Docs-directory resolution ─────────────────────────────────────────────────

def _find_docs_dir(package_name: str) -> Path | None:
    """Return the Starlight content directory for *package_name*, or ``None``."""
    if package_name == "lexigram":
        return CONTENT_ROOT / "packages/foundation/lexigram"

    for path in CONTENT_ROOT.rglob("*"):
        if path.is_dir() and path.name == package_name and "api" not in path.parts:
            return path

    # lexigram-ai-* packages live under platform/
    if package_name.startswith("lexigram-ai"):
        for path in (CONTENT_ROOT / "platform").rglob("*"):
            if path.is_dir() and path.name == package_name:
                return path

    # Strip the "lexigram-" prefix and retry
    short = package_name.replace("lexigram-", "")
    for path in CONTENT_ROOT.rglob("*"):
        if path.is_dir() and path.name == short and "api" not in path.parts:
            return path

    return None


# ── Shim detection ────────────────────────────────────────────────────────────

def _is_shim(file_path: Path) -> bool:
    """Return ``True`` when *file_path* is a namespace-package shim with no exports."""
    content     = file_path.read_text()
    has_exports = any(tok in content for tok in ("__all__", "_LAZY_IMPORTS", "_EXPORTS"))

    if "namespace package" in content.lower() and not has_exports:
        return True
    if "Namespace package shim" in content:
        return True
    if "pkgutil.extend_path" in content and not has_exports and len(content) < 500:
        return True
    if not has_exports and len(content.strip()) < 100:
        return True

    return False


def _find_non_shim_roots(directory: Path, result: list[Path]) -> None:
    """Populate *result* with the highest-level non-shim ``__init__.py`` files
    found under *directory* (recursive, stops at each non-shim root)."""
    init = directory / "__init__.py"
    if init.exists():
        if not _is_shim(init):
            result.append(init)
            return                      # stop descending — this is the root

    for sub in directory.iterdir():
        if sub.is_dir() and not sub.name.startswith(("_", ".")) and "docs" not in sub.name:
            _find_non_shim_roots(sub, result)


# ── HTML / signature rendering ────────────────────────────────────────────────

#: CSS helpers for API table cells.
_L  = (
    "display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;"
    "text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;"
)
_T  = "border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;"
_TH = "text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);"
_TN = "padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);"
_TT = "padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);"
_TD = "padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);"

#: Signature token colours — CSS variable references.
_C_NAME    = "color: var(--lex-color-name)"
_C_COLON   = "color: var(--lex-color-colon)"
_C_TYPE    = "color: var(--lex-color-type)"
_C_DEFAULT = "color: var(--lex-color-default) !important"
_C_STRING  = "color: var(--lex-color-string) !important"
_C_RETURN  = "color: var(--lex-color-return)"
_C_FNAME   = "color: var(--lex-color-fname); font-weight: 600"
_C_KEYWORD = "color: var(--lex-color-keyword)"


def _span(text: str, css: str) -> str:
    return f"<span style='{css}'>{text}</span>"


def _make_sig_box(
    sig_html: str,
    label: str = "signature",
    font_size: str = "0.9em",
    margin_bottom: str = "1.5rem",
) -> str:
    """Render a signature block styled like an Expressive Code frame."""
    _dots = (
        "display:inline-block;width:12px;height:12px;border-radius:50%;"
        "background-color:#ff5f56;"
        "box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;"
    )
    header = (
        f"<div style='background:var(--color-background-weak);"
        f"border-bottom:1px solid var(--color-border-weak);"
        f"padding:0 1rem;min-height:36px;display:flex;align-items:center;"
        f"padding-left:70px;position:relative;'>"
        f"<span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);{_dots}'></span>"
        f"<span style='font-family:var(--sl-font-mono);font-size:0.72em;"
        f"color:var(--color-text-weaker);'>{label}</span>"
        f"</div>"
    )
    pre = (
        f"<pre style='margin:0;background:var(--color-background-weak);"
        f"font-family:var(--sl-font-mono);font-size:{font_size};"
        f"line-height:1.65;white-space:pre-wrap;word-break:break-all;"
        f"padding:0.75rem 1rem;'>{sig_html}</pre>"
    )
    return (
        f"<div style='border-radius:8px;border:1px solid var(--color-border-weak);"
        f"overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);"
        f"margin-bottom:{margin_bottom};'>"
        f"{header}{pre}</div>\n"
    )


def _linkify_type(t_str: str, global_symbols: dict) -> str:
    """Wrap known symbol names in hyperlinks and colour special tokens."""
    if not t_str:
        return ""

    words = set(re.findall(r"[a-zA-Z0-9_]+", t_str))
    res   = t_str
    links: dict[str, str] = {}

    # Replace known symbols with unique placeholders to avoid nested replacements.
    for w in sorted(words, key=len, reverse=True):
        if w in global_symbols and global_symbols[w]:
            placeholder = f"__SYM_{w}__"
            res = re.sub(rf"\b{w}\b", placeholder, res)
            links[placeholder] = (
                f"<a href='{global_symbols[w]}' style='color:inherit;"
                f"text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);"
                f"text-underline-offset:2px;'>{w}</a>"
            )

    # Colour structural tokens.
    res = res.replace(" | ", f" <span style='{_C_COLON}'>|</span> ")
    res = res.replace("|",   f"<span style='{_C_COLON}'>|</span>")
    res = re.sub(r"\bNone\b",  _span("None",  _C_DEFAULT), res)
    res = re.sub(r"\bTrue\b",  _span("True",  _C_DEFAULT), res)
    res = re.sub(r"\bFalse\b", _span("False", _C_DEFAULT), res)
    res = res.replace("[", f"<span style='{_C_COLON}'>[</span>")
    res = res.replace("]", f"<span style='{_C_COLON}'>]</span>")
    res = res.replace(",", f"<span style='{_C_COLON}'>,</span>")

    # Restore hyperlinks.
    for placeholder, link_html in links.items():
        res = res.replace(placeholder, link_html)

    return res


def _style_value(v: str) -> str:
    """Return a coloured ``<span>`` for a default-value token."""
    v = v.strip()
    if v in ("None", "True", "False") or v.replace(".", "", 1).isdigit():
        return _span(v, _C_DEFAULT)
    if (v.startswith("'") and v.endswith("'")) or (v.startswith('"') and v.endswith('"')):
        return _span(v, _C_STRING)
    return _span(v, _C_DEFAULT)


def _render_param(p: str, global_symbols: dict) -> str:
    """Render a single parameter token as highlighted HTML."""
    prefix_raw = ""
    if p.startswith("**"):
        prefix_raw, p = "**", p[2:]
    elif p.startswith("*"):
        prefix_raw, p = "*", p[1:]

    prefix_html = _span(prefix_raw, _C_DEFAULT) if prefix_raw else ""

    if ":" in p:
        n, rest = p.split(":", 1)
        if "=" in rest:
            t, d = rest.split("=", 1)
            return (
                prefix_html
                + _span(n.strip(), _C_NAME)
                + _span(": ", _C_COLON)
                + _span(_linkify_type(t.strip(), global_symbols), _C_TYPE)
                + _span(" = ", _C_COLON)
                + _style_value(d)
            )
        return (
            prefix_html
            + _span(n.strip(), _C_NAME)
            + _span(": ", _C_COLON)
            + _span(_linkify_type(rest.strip(), global_symbols), _C_TYPE)
        )

    if "=" in p:
        n, d = p.split("=", 1)
        return prefix_html + _span(n.strip(), _C_NAME) + _span("=", _C_COLON) + _style_value(d)

    return prefix_html + _span(p, _C_NAME)


def _split_params(inner: str) -> list[str]:
    """Split a parameter string on commas, respecting nested brackets."""
    params: list[str] = []
    depth   = 0
    current: list[str] = []
    for ch in inner:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            params.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        params.append("".join(current).strip())
    return params


def render_signature_html(
    name:           str,
    sig_plain:      str,
    global_symbols: dict,
    is_async:       bool = False,
    is_property:    bool = False,
) -> str:
    """Return a pretty-printed, syntax-highlighted HTML snippet for a signature."""
    prefix_html = ""
    if is_async:
        prefix_html += _span("async ", _C_KEYWORD)
    if is_property:
        prefix_html += _span("property ", _C_KEYWORD)
    else:
        prefix_html += _span("def ", _C_KEYWORD)

    name_html = _span(name, _C_FNAME)

    if not sig_plain or sig_plain == "()":
        return f"{prefix_html}{name_html}<span style='{_C_COLON}'>()</span>"

    # Strip the return annotation so we can colour it separately.
    ret_html = ""
    body     = sig_plain
    if not body.endswith(")"):
        arrow = body.rfind(") ->")
        if arrow != -1:
            ret_raw = body[arrow + 4:].strip()
            body    = body[: arrow + 1]
            if ret_raw == "None":
                ret_html = _span(" -> ", _C_KEYWORD) + _span("None", _C_DEFAULT)
            else:
                ret_html = (
                    _span(" -> ", _C_KEYWORD)
                    + _span(_linkify_type(ret_raw, global_symbols), _C_RETURN)
                )

    inner = body.strip()
    if inner.startswith("(") and inner.endswith(")"):
        inner = inner[1:-1]

    params    = _split_params(inner)
    open_p    = _span("(", _C_COLON)
    close_p   = _span(")", _C_COLON)
    comma     = _span(",", _C_COLON)

    if len(params) <= 1:
        inner_html = _render_param(params[0], global_symbols) if params else ""
        return f"{prefix_html}{name_html}{open_p}{inner_html}{close_p}{ret_html}"

    indent = "    "
    lines  = [f"{prefix_html}{name_html}{open_p}"]
    for i, p in enumerate(params):
        trail = comma if i < len(params) - 1 else ""
        lines.append(f"{indent}{_render_param(p, global_symbols)}{trail}")
    lines.append(f"{close_p}{ret_html}")
    return "\n".join(lines)


# ── Docstring processing ──────────────────────────────────────────────────────

def _make_table(label: str, headers: list[str], rows_html: list[str]) -> str:
    """Render a labelled HTML table for Parameters / Returns / Raises sections."""
    ths: list[str] = []
    for i, h in enumerate(headers):
        style = _TH
        if h == "Description":
            style += "padding-left:1.2rem;border-left:1px solid var(--color-border-weak);"
        # Fixed column widths keep the "Description" axis aligned across tables.
        if len(headers) == 3:          # Parameters
            style += ("width:20%;" if i == 0 else "width:25%;" if i == 1 else "width:55%;")
        elif len(headers) == 2:        # Returns / Raises
            style += ("width:45%;" if i == 0 else "width:55%;")
        ths.append(f"<th style='{style}'>{h}</th>")

    ths_html = "".join(ths)
    rows     = "".join(rows_html)
    return (
        f"\n\n<div style='margin:0;line-height:1.4;'>"
        f"<span style='{_L}'>{label}</span>"
        f"<table style='{_T}'><thead><tr>{ths_html}</tr></thead>"
        f"<tbody>{rows}</tbody></table></div>\n\n"
    )


def _handle_role(m: re.Match, global_symbols: dict) -> str:
    """Replace a Sphinx ``:role:`target``` with a linkified display name."""
    target       = m.group(1)
    display_name = target.split(".")[-1] if target.startswith("~") else target
    return _linkify_type(display_name, global_symbols)


def process_docstring(
    clean_doc:      str,
    global_symbols: dict | None = None,
    param_types:    dict | None = None,
) -> str:
    """Convert a raw Python docstring into MDX-ready HTML + Markdown.

    Handles Google-style ``Args:``, ``Returns:``, ``Raises:``, REPL examples,
    ``::`` code blocks, and Sphinx cross-reference roles.
    """
    if not clean_doc:
        return ""
    if global_symbols is None:
        global_symbols = {}
    if param_types is None:
        param_types = {}

    # Sphinx roles → linkified names
    clean_doc = re.sub(
        r":(?:class|func|meth|mod|attr|obj):`([^`]+)`",
        lambda m: _handle_role(m, global_symbols),
        clean_doc,
    )
    # RST admonitions → Markdown blockquotes
    clean_doc = re.sub(
        r"^\s*\.\.\s+(note|warning|important|tip)::\s*",
        lambda m: f"> **{m.group(1).capitalize()}**\n> ",
        clean_doc,
        flags=re.MULTILINE,
    )

    lines = clean_doc.split("\n")
    out: list[str] = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()

        # ── Args / Parameters ──────────────────────────────────────────────
        if stripped in ("Args:", "Parameters:"):
            rows: list[str] = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i][0] in " \t"):
                item = lines[i].strip()
                if item:
                    m = re.match(r"^`?([\w_]+)`?\s*(?:\(([^)]+)\))?:\s*(.*)", item)
                    if m:
                        p_name, p_type, p_desc = m.group(1), m.group(2), m.group(3)
                        if not p_type and p_name in param_types:
                            p_type = param_types[p_name]
                        rows.append(
                            f"<tr>"
                            f"<td style='{_TN}'>`{p_name}`</td>"
                            f"<td style='{_TT}'>{_linkify_type(p_type or '', global_symbols)}</td>"
                            f"<td style='{_TD}'>{p_desc}</td>"
                            f"</tr>"
                        )
                    elif rows:
                        rows[-1] = rows[-1].replace("</td></tr>", f" {item}</td></tr>", 1)
                i += 1
            out.append(_make_table("Parameters", ["Parameter", "Type", "Description"], rows))
            continue

        # ── Returns / Yields ───────────────────────────────────────────────
        if stripped in ("Returns:", "Yields:"):
            label        = stripped.rstrip(":")
            rows         = []
            is_first     = True
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i][0] in " \t"):
                item = lines[i].strip()
                if item:
                    m = re.match(r"^([\w_\[\], |]+):\s*(.*)", item)
                    if m:
                        r_type = m.group(1).strip()
                        r_desc = m.group(2).strip()
                        if r_type in ("Returns", "Yields", "") and "__return__" in param_types:
                            r_type = param_types["__return__"]
                        rows.append(
                            f"<tr>"
                            f"<td style='{_TT}'>{_linkify_type(r_type, global_symbols)}</td>"
                            f"<td style='{_TD}'>{r_desc}</td>"
                            f"</tr>"
                        )
                    else:
                        r_type = param_types.get("__return__", "") if is_first else ""
                        if is_first:
                            rows.append(
                                f"<tr>"
                                f"<td style='{_TT}'>{_linkify_type(r_type, global_symbols)}</td>"
                                f"<td style='{_TD}'>{item}</td>"
                                f"</tr>"
                            )
                        elif rows:
                            rows[-1] = rows[-1].replace("</td></tr>", f" {item}</td></tr>", 1)
                    is_first = False
                i += 1
            out.append(_make_table(label, ["Type", "Description"], rows))
            continue

        # ── Raises ─────────────────────────────────────────────────────────
        if stripped == "Raises:":
            rows = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i][0] in " \t"):
                item = lines[i].strip()
                if item:
                    m = re.match(r"^([\w_.]+):\s*(.*)", item)
                    if m:
                        rows.append(
                            f"<tr>"
                            f"<td style='{_TT}'>{_linkify_type(m.group(1), global_symbols)}</td>"
                            f"<td style='{_TD}'>{m.group(2)}</td>"
                            f"</tr>"
                        )
                    elif rows:
                        rows[-1] = rows[-1].replace("</td></tr>", f" {item}</td></tr>", 1)
                i += 1
            out.append(_make_table("Raises", ["Exception", "Description"], rows))
            continue

        # ── Examples / Notes / Warnings ────────────────────────────────────
        if stripped in ("Example:", "Examples:", "Usage:", "Note:", "Warning:"):
            out.append(f"\n**{stripped.rstrip(':')}**\n")
            i += 1
            block_lines: list[str] = []
            repl_lines:  list[str] = []
            is_repl = False

            while i < len(lines):
                line    = lines[i]
                s_line  = line.strip()
                if not s_line:
                    (repl_lines if is_repl else block_lines).append(line)
                elif s_line.startswith(">>>") or s_line.startswith("..."):
                    is_repl = True
                    repl_lines.append(line)
                elif is_repl:
                    break
                elif line.startswith("    ") or line.startswith("\t"):
                    block_lines.append(line)
                else:
                    break
                i += 1

            if is_repl and repl_lines:
                code: list[str] = []
                for line in repl_lines:
                    sl = line.strip()
                    if sl.startswith(">>>"):
                        code.append(sl[3:].lstrip())
                    elif sl.startswith("..."):
                        code.append(sl[3:].lstrip())
                    else:
                        code.append(line.rstrip())
                out.append("```python\n" + "\n".join(code) + "\n```")
            elif block_lines:
                out.append(textwrap.dedent("\n".join(block_lines)))
            continue

        out.append(lines[i])
        i += 1

    # ── RST :: code blocks → fenced Markdown ──────────────────────────────
    result_lines: list[str] = []
    joined = "\n".join(out)
    for i, line in enumerate(joined.split("\n")):
        if line.strip().endswith("::"):
            result_lines.append(line.rstrip(":"))
            # consume following indented block
            block: list[str] = []
            i += 1
            src = joined.split("\n")
            while i < len(src) and (not src[i].strip() or src[i].startswith("    ") or src[i].startswith("\t")):
                block.append(src[i])
                i += 1
            if block:
                result_lines.append("\n```python")
                result_lines.append(textwrap.dedent("\n".join(block)).strip())
                result_lines.append("```\n")
            continue
        result_lines.append(line)

    # ── Ensure bare ``` fences become ```python ────────────────────────────
    formatted: list[str] = []
    in_cb = False
    for line in result_lines:
        s = line.strip()
        if s.startswith("```"):
            in_cb = not in_cb
            if in_cb and s == "```":
                line = line.replace("```", "```python")
        formatted.append(line)

    return "\n".join(formatted)


# ── init.py parser ────────────────────────────────────────────────────────────

def _parse_init(
    init_path:    Path,
    package_name: str,
    module_prefix: str,
) -> tuple[list[str], dict[str, tuple[str, str]]]:
    """Parse an ``__init__.py`` file and return ``(exported_names, lazy_imports)``.

    *lazy_imports* maps each exported name to ``(source_module, real_name)``.
    """
    try:
        tree = ast.parse(init_path.read_text())
    except Exception:
        return [], {}

    exported_names: list[str]                  = []
    lazy_imports:   dict[str, tuple[str, str]] = {}
    merge_lazy      = False

    for node in tree.body:
        tid: str | None  = None
        val              = None

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    tid, val = target.id, node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            tid, val = node.target.id, node.value

        if tid is None or val is None:
            continue

        # __all__
        if tid == "__all__" and isinstance(val, (ast.List, ast.Set)):
            for elt in val.elts:
                if isinstance(elt, (ast.Constant, ast.Str)):
                    v = getattr(elt, "value", getattr(elt, "s", None))
                    if isinstance(v, str):
                        exported_names.append(v)
                elif isinstance(elt, ast.Starred):
                    merge_lazy = True

        # _LAZY_IMPORTS / _EXPORTS / _LAZY_SUBMODULES
        if tid in ("_LAZY_IMPORTS", "_EXPORTS", "_LAZY_SUBMODULES") and isinstance(val, ast.Dict):
            for k, v in zip(val.keys, val.values):
                key = getattr(k, "value", getattr(k, "s", None))
                if not key:
                    continue
                if isinstance(v, ast.Constant):
                    lazy_imports[key] = (v.value, key)
                elif isinstance(v, ast.Tuple) and len(v.elts) >= 2:
                    v_mod  = getattr(v.elts[0], "value", getattr(v.elts[0], "s", None))
                    v_attr = getattr(v.elts[1], "value", getattr(v.elts[1], "s", None))
                    if v_mod and v_attr:
                        lazy_imports[key] = (v_mod, v_attr)
                elif isinstance(v, (ast.Constant, ast.Str)):
                    v_val = getattr(v, "value", getattr(v, "s", None))
                    if v_val:
                        lazy_imports[key] = (v_val, key)

    # Merge lazy keys into __all__ when a Starred expression was present.
    if merge_lazy:
        exported_names = list(set(exported_names) | set(lazy_imports.keys()))
    elif not exported_names and lazy_imports:
        exported_names = list(lazy_imports.keys())

    # Guarantee all names are plain strings.
    exported_names = [n for n in exported_names if isinstance(n, str)]

    print(f"      [?] {package_name} ({module_prefix}): {len(exported_names)} exports")
    return exported_names, lazy_imports


# ── Markdown generation ───────────────────────────────────────────────────────

#: Per-page <style> injected via Starlight frontmatter.
_PAGE_STYLE = (
    "head:\n"
    "  - tag: style\n"
    "    content: |\n"
    "      .sl-markdown-content p,\n"
    "      .sl-markdown-content li,\n"
    "      .sl-markdown-content td,\n"
    "      .sl-markdown-content th,\n"
    "      .sl-markdown-content blockquote,\n"
    "      .sl-markdown-content dt,\n"
    "      .sl-markdown-content dd {\n"
    "        font-family: var(--sl-font-mono) !important;\n"
    "        font-size: 0.9rem;\n"
    "        line-height: 1.65;\n"
    "      }\n"
    "      .sl-markdown-content code {\n"
    "        font-size: 0.88em;\n"
    "      }\n"
)

_GROUP_ORDER = ["Protocols", "Classes", "Functions", "Exceptions"]


def _render_item(
    name:           str,
    info:           dict,
    global_symbols: dict,
) -> str:
    """Return the full MDX block for a single API symbol."""
    signature  = info["signature"]
    docstring  = info["docstring"]
    is_async   = info["is_async"]
    methods    = info["methods"]
    p_types    = info.get("param_types", {})
    github_url = info["github_url"]

    clean_doc  = process_docstring(docstring, global_symbols, p_types)
    type_meta  = f"<span data-api-type='{info['group']}' style='display:none;'></span>"
    anchor_id  = re.sub(r"[^a-z0-9]", "", name.lower())
    heading    = f"<div data-pagefind-weight='10'>\n\n### `{name}`\n\n</div>\n\n{type_meta}\n\n"

    gh_badge = ""
    if github_url:
        gh_badge = (
            f"<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'>"
            f"<a href='{github_url}' target='_blank' rel='noopener noreferrer' "
            f"style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;"
            f"color:var(--sl-color-gray-3);text-decoration:none;'>"
            f"<svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>"
            f"source</a></div>"
        )

    if signature:
        sig_html  = render_signature_html(name, signature, global_symbols, is_async=is_async)
        sig_box   = _make_sig_box(sig_html, label=name, margin_bottom="1.5rem")
        body      = f"{heading}{sig_box}\n{gh_badge}\n{clean_doc}\n"
    else:
        body      = f"{heading}{gh_badge}\n{clean_doc}\n"

    if methods:
        method_blocks: list[str] = []
        for m in methods:
            m_sig_html = render_signature_html(
                m["name"], m["signature"], global_symbols,
                is_async=m["is_async"], is_property=m["is_property"],
            )
            m_sig_box = _make_sig_box(m_sig_html, label=m["name"], font_size="0.875em", margin_bottom="1rem")
            m_doc     = process_docstring(m["docstring"], global_symbols, m.get("param_types", {}))
            m_gh = ""
            if m.get("github_url"):
                m_gh = (
                    f"<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'>"
                    f"<a href='{m['github_url']}' target='_blank' rel='noopener noreferrer' "
                    f"style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;"
                    f"color:var(--sl-color-gray-3);text-decoration:none;'>"
                    f"<svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>"
                    f"source</a></div>"
                )
            method_blocks.append(f"{m_sig_box}\n{m_gh}\n\n{m_doc}")

        body += (
            "\n<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);"
            "margin-top:2rem;margin-bottom:2rem;'>\n"
            + "\n\n".join(method_blocks)
            + "\n</div>\n"
        )

    divider = "\n<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />\n"
    return body + divider


def _write_api_page(target_dir: Path, groups: dict) -> None:
    """Render and write ``api.md`` for a single package docs directory."""
    sections: list[str] = []
    existing  = [g for g in _GROUP_ORDER if g in groups]
    extra     = sorted(g for g in groups if g not in _GROUP_ORDER)

    # PASS 1 — build cross-link symbol map
    global_symbols: dict[str, str | None] = {}
    for group_name, item_dict in groups.items():
        for name in item_dict:
            anchor = re.sub(r"[^a-z0-9]", "", name.lower())
            url    = "/" + str(target_dir.relative_to(CONTENT_ROOT)) + f"/api/#{anchor}"
            global_symbols[name] = url if name not in global_symbols else None

    # PASS 2 — render each group
    for group_name in existing + extra:
        item_dict = groups.get(group_name, {})
        if not item_dict:
            continue
        items_md = [f"## {group_name}\n\n"]
        for name in sorted(item_dict):
            items_md.append(_render_item(name, item_dict[name], global_symbols))
        sections.append("\n".join(items_md))

    pkg_name   = target_dir.name
    frontmatter = (
        f"---\n"
        f"title: API Reference\n"
        f"description: Complete API reference for the {pkg_name} package.\n"
        f"sidebar:\n"
        f"  hidden: true\n"
        f"{_PAGE_STYLE}"
        f"---\n\n"
    )
    content = frontmatter + "\n".join(sections)

    # Remove any stale .mdx file first.
    mdx = target_dir / "api.mdx"
    if mdx.exists():
        mdx.unlink()

    (target_dir / "api.md").write_text(content)
    print(f"  [✓] Wrote {target_dir.relative_to(CONTENT_ROOT)}/api.md")


# ── Entry point ───────────────────────────────────────────────────────────────

def generate_api() -> None:
    """Main entry point — walk the monorepo and emit one api.md per package."""
    print(f"Generating API reference …")
    print(f"  Framework root : {FRAMEWORK_ROOT}")
    print(f"  Content root   : {CONTENT_ROOT}\n")

    packages = sorted(
        d.name for d in FRAMEWORK_ROOT.iterdir()
        if d.is_dir() and d.name.startswith("lexigram") and d.name not in _PROPRIETARY_PKGS
    )

    # Maps target_dir → {group → {name → info}}
    aggregated: dict[Path, dict[str, dict]] = {}

    for package_name in packages:
        src_lexigram = FRAMEWORK_ROOT / package_name / "src" / "lexigram"
        if not src_lexigram.exists():
            continue

        init_files: list[Path] = []
        _find_non_shim_roots(src_lexigram, init_files)

        for init_path in init_files:
            rel_parts     = init_path.relative_to(FRAMEWORK_ROOT / package_name / "src").parts
            module_prefix = ".".join(p for p in rel_parts if p != "__init__.py")

            exported_names, lazy_imports = _parse_init(init_path, package_name, module_prefix)
            if not exported_names:
                print(f"  [-] Skipped {package_name} ({module_prefix}): nothing exported")
                continue

            target_dir = _find_docs_dir(package_name) or _find_docs_dir(module_prefix.split(".")[-1])
            if not target_dir:
                print(f"  [!] No docs dir found for {package_name}")
                continue

            if target_dir not in aggregated:
                aggregated[target_dir] = {}

            count = 0
            for name in sorted(exported_names):
                mod_info                    = lazy_imports.get(name)
                module_path, real_name      = mod_info if mod_info else (module_prefix, name)
                result                      = _find_definition(module_path, real_name)
                if not result:
                    print(f"    [!] Could not resolve {name} from {module_path}")
                    continue

                group = result["group"]
                aggregated[target_dir].setdefault(group, {})
                aggregated[target_dir][group][name] = result
                count += 1

            print(f"  [>] {package_name} → {target_dir.relative_to(CONTENT_ROOT)} ({count} items)")

    for target_dir, groups in aggregated.items():
        _write_api_page(target_dir, groups)

    print("\nDone.")


if __name__ == "__main__":
    generate_api()