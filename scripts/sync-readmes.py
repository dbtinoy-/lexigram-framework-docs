import os
import re
from pathlib import Path

# Paths
DOCS_ROOT = Path(__file__).parent.parent
# Allow override via environment variable for CI/CD environments like Cloudflare
FRAMEWORK_ROOT = Path(os.environ.get("LEX_ROOT", str(DOCS_ROOT.parent / "lexigram")))
CONTENT_ROOT = DOCS_ROOT / "src/content/docs"

def get_frontmatter_and_content(file_path):
    if not file_path.exists():
        return None, None
    content = file_path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n*(.*)", content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def find_target_file(package_name):
    """Search for a directory named package_name under CONTENT_ROOT and return its index file."""
    for path in CONTENT_ROOT.rglob(package_name):
        if path.is_dir():
            target_file = path / "index.md"
            if target_file.exists():
                return target_file
            target_file = path / "index.mdx"
            if target_file.exists():
                return target_file
    return None

def humanize(label):
    if label == 'lexigram': return 'Core (lexigram)'
    if not label.startswith('lexigram-'): return label
    
    mapping = {
        'lexigram-foundation': 'Foundation',
        'lexigram-web': 'Web',
        'lexigram-data': 'Data',
        'lexigram-security': 'Security',
        'lexigram-events': 'Events',
        'lexigram-infra': 'Infrastructure',
        'lexigram-utilities': 'Utilities',
        'lexigram-ai': 'AI',
        'lexigram-admin': 'Admin',
        'lexigram-cli': 'CLI',
        'lexigram-ui': 'UI',
        'lexigram-testing': 'Testing',
        'lexigram-contracts': 'Contracts',
    }
    
    base = mapping.get(label)
    if not base:
        p = label.replace('lexigram-', '').split('-')
        parts = []
        for part in p:
            if part in ['ai', 'ui', 'cli', 'http', 'sql', 'nosql', 'sse', 'mcp']:
                parts.append(part.upper())
            else:
                parts.append(part.capitalize())
        base = ' '.join(parts)
    
    return f"{base} ({label})"

# Proprietary / never-published packages — excluded from docs generation.
PROPRIETARY_PKGS = frozenset({
    "lexigram-ai-guard", "lexigram-ai-governance",
    "lexigram-ai-evaluation", "lexigram-ai-prompt",
})


def sync_readmes():
    print(f"Syncing READMEs, docs, and cleaning up frontmatter...")
    
    if not FRAMEWORK_ROOT.exists():
        print(f"Error: Framework root {FRAMEWORK_ROOT} not found.")
        return

    packages = sorted(
        d.name for d in FRAMEWORK_ROOT.iterdir()
        if d.is_dir() and d.name.startswith("lexigram") and d.name not in PROPRIETARY_PKGS
    )
    
    for package_name in sorted(packages):
        target_file = find_target_file(package_name)
        if not target_file:
            continue

        target_dir = target_file.parent
        
        # 1. Sync README.md
        readme_path = FRAMEWORK_ROOT / package_name / "README.md"
        if readme_path.exists():
            fm_text, _ = get_frontmatter_and_content(target_file)
            
            # Update title and remove hero
            humanized_title = humanize(package_name)
            
            # Remove existing hero section if present
            if fm_text:
                fm_text = re.sub(r"hero:.*?(?=^[\w\-]+:|\Z)", "", fm_text, flags=re.DOTALL | re.MULTILINE)
                fm_text = re.sub(r"^title:.*", f"title: {humanized_title}", fm_text, flags=re.MULTILINE)
                if "title:" not in fm_text:
                    fm_text = f"title: {humanized_title}\n" + fm_text
            else:
                fm_text = f"title: {humanized_title}\ndescription: Detailed documentation for {package_name}, including architecture, usage guides, and configuration options within the Lexigram ecosystem."
                
            readme_content = readme_path.read_text()
            readme_content = re.sub(r"^# .*\n", "", readme_content, count=1)
            new_content = f"---\n{fm_text.strip()}\n---\n\n{readme_content.strip()}"
            
            target_file.write_text(new_content)
            print(f"  [✓] Synced & Cleaned: {package_name}/README.md -> {target_file.relative_to(DOCS_ROOT)}")

        # 2. Sync docs/ folder
        docs_path = FRAMEWORK_ROOT / package_name / "docs"
        if docs_path.exists() and docs_path.is_dir():
            target_docs_dir = target_dir / "docs"
            target_docs_dir.mkdir(exist_ok=True)
            
            for doc_file in docs_path.glob("*.md"):
                target_doc_file = target_docs_dir / doc_file.name
                
                doc_fm_text, _ = get_frontmatter_and_content(target_doc_file)
                doc_content = doc_file.read_text()
                
                title_match = re.search(r"^# (.*)", doc_content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else doc_file.stem.replace('-', ' ').title()
                
                # Strip existing frontmatter from source content to avoid double frontmatter
                doc_content = re.sub(r"^---\n.*?\n---\n*", "", doc_content, flags=re.DOTALL)
                doc_content = re.sub(r"^# .*\n", "", doc_content, count=1)
                
                # Quote YAML values that could break parsing (trailing colons, etc.)
                safe_title = f"'{title}'" if title.endswith(':') else title
                
                if not doc_fm_text:
                    desc = f"{title} guide and reference for the {package_name} package in the Lexigram framework."
                    safe_desc = f"'{desc}'" if ':' in desc else desc
                    doc_fm_text = f"title: {safe_title}\ndescription: {safe_desc}"
                
                new_doc_content = f"---\n{doc_fm_text.strip()}\n---\n\n{doc_content.strip()}"
                
                target_doc_file.write_text(new_doc_content)
                print(f"  [✓] Synced Doc: {package_name}/docs/{doc_file.name} -> {target_doc_file.relative_to(DOCS_ROOT)}")

def sync_error_codes():
    """Sync REF_ERROR_CODES.md to reference/errors.md with anchor links."""
    error_codes_path = FRAMEWORK_ROOT / "docs" / "lexigram-docs" / "reference" / "REF_ERROR_CODES.md"
    if not error_codes_path.exists():
        print(f"  [!] REF_ERROR_CODES.md not found at {error_codes_path}")
        return
    
    target_dir = CONTENT_ROOT / "reference"
    target_dir.mkdir(exist_ok=True)
    target_file = target_dir / "errors.md"
    
    content = error_codes_path.read_text()
    
    # Convert markdown tables to have anchor links for each error code
    lines = content.split('\n')
    new_lines = []
    in_table = False
    
    for line in lines:
        if '|:-----|:------|' in line or '| Code |' in line:
            in_table = True
            new_lines.append(line)
            continue
        
        if in_table and not line.strip().startswith('|'):
            in_table = False
        
        if in_table and line.strip().startswith('|') and '`' in line:
            line = re.sub(
                r'`(LEX_ERR_[A-Z]+_\d+)`',
                r'<a href="#\1" class="error-code">`\1`</a>',
                line
            )
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    frontmatter = """---
title: Error Codes
description: Complete registry of all LEX_ERR_* error codes in the Lexigram Framework.
sidebar:
  order: 2
---

"""
    
    content = re.sub(r'^# .*\n', '', content, count=1)
    
    final_content = frontmatter + content.strip()
    target_file.write_text(final_content)
    print(f"  [✓] Synced Error Codes: REF_ERROR_CODES.md -> reference/errors.md")


def sync_cli_commands():
    """Sync REF_CLI_COMMANDS.md to reference/cli.md."""
    cli_cmds_path = FRAMEWORK_ROOT / "docs" / "lexigram-docs" / "reference" / "REF_CLI_COMMANDS.md"
    if not cli_cmds_path.exists():
        print(f"  [!] REF_CLI_COMMANDS.md not found at {cli_cmds_path}")
        return

    target_dir = CONTENT_ROOT / "reference"
    target_dir.mkdir(exist_ok=True)
    target_file = target_dir / "cli.md"

    content = cli_cmds_path.read_text()

    frontmatter = """---
title: CLI Reference
description: Complete command registry — all CLI commands, subcommands, and generators across the Lexigram Framework.
sidebar:
  order: 3
---

"""
    content = re.sub(r'^# .*\n', '', content, count=1)
    final_content = frontmatter + content.strip()
    target_file.write_text(final_content)
    print(f"  [✓] Synced CLI Commands: REF_CLI_COMMANDS.md -> reference/cli.md")


def sync_env_vars():
    """Sync REF_ENV_VARS.md to reference/env-vars.md."""
    env_vars_path = FRAMEWORK_ROOT / "docs" / "lexigram-docs" / "reference" / "REF_ENV_VARS.md"
    if not env_vars_path.exists():
        print(f"  [!] REF_ENV_VARS.md not found at {env_vars_path}")
        return
    
    target_dir = CONTENT_ROOT / "reference"
    target_dir.mkdir(exist_ok=True)
    target_file = target_dir / "env-vars.md"
    
    content = env_vars_path.read_text()
    
    frontmatter = """---
title: Environment Variables
description: Complete registry of all environment variables in the Lexigram Framework.
sidebar:
  order: 4
---

:::note
This document is auto-generated from source. Last updated: 2026-05-27.
:::

"""
    
    content = re.sub(r'^# .*\n', '', content, count=1)
    
    final_content = frontmatter + content.strip()
    target_file.write_text(final_content)
    print(f"  [✓] Synced Environment Variables: REF_ENV_VARS.md -> reference/env-vars.md")


def _strip_proprietary(content: str) -> str:
    """Remove proprietary package rows from markdown tables and update counts."""
    lines = content.split("\n")

    # Strip full detailed sections for proprietary packages
    # (### Package tests: lexigram-admin + all content until next ### or EOF)
    filtered: list[str] = []
    skip_section = False
    for line in lines:
        m = re.match(r"^### Package tests: (\S+)", line)
        if m:
            skip_section = m.group(1) in PROPRIETARY_PKGS
        if skip_section:
            continue
        filtered.append(line)
    lines = filtered

    result: list[str] = []
    total = len(PROPRIETARY_PKGS)
    open_count = 43 - total

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|"):
            # Check for backtick-wrapped package names: | `lexigram-admin` | ...
            if "`" in stripped:
                pkg = stripped.split("`")[1] if stripped.count("`") >= 2 else ""
                if pkg in PROPRIETARY_PKGS:
                    continue
            # Check for plain-text package names: | Package tests: lexigram-admin | ...
            found = False
            for p in PROPRIETARY_PKGS:
                # Match cell containing the package name as a word (not substring)
                if re.search(rf"(^|\|)\s*.*\b{re.escape(p)}\b.*\|", stripped):
                    found = True
                    break
            if found:
                continue
        # Update count references
        if "all 43 packages" in stripped:
            line = line.replace("all 43 packages", f"all {open_count} open-source packages")
        if "43 packages" in stripped or "Packages counted: 43" in stripped:
            line = line.replace("43 packages", f"{open_count} packages")
            line = line.replace("Packages counted: 43", f"Packages counted: {open_count}")
        if re.match(r"^\|.*\|.*\|.*\|$", stripped) and "packages" in stripped.lower():
            line = re.sub(r"\b43\b", str(open_count), line)
        result.append(line)
    return "\n".join(result)


def _audit_title(name: str) -> str:
    be = name.removeprefix("AUDIT_").removesuffix(".md").removesuffix(".json").replace("_", " ").title()
    if be.lower() == "index":
        return "Audit Index"
    return be + " Audit"


def sync_audit_files():
    """Sync all AUDIT_* and index.* files from docs/lexigram-docs/audit to audit/."""
    src = FRAMEWORK_ROOT / "docs" / "lexigram-docs" / "audit"
    if not src.exists():
        print(f"  [!] Audit source not found at {src}")
        return

    target_dir = CONTENT_ROOT / "audit"
    target_dir.mkdir(exist_ok=True)
    count = 0

    for srcfile in sorted(src.iterdir()):
        if not srcfile.is_file():
            continue

        if srcfile.name == "index.json":
            tgt = target_dir / "index.json"
            tgt.write_bytes(srcfile.read_bytes())
            print(f"  [✓] Synced: {srcfile.name} -> audit/index.json")
            count += 1
            continue

        if srcfile.suffix != ".md":
            continue

        target_name = srcfile.name
        if target_name.startswith("AUDIT_"):
            target_name = target_name.removeprefix("AUDIT_").lower()
        elif target_name == "index.md":
            target_name = "index.md"

        content = _strip_proprietary(srcfile.read_text())
        title = _audit_title(srcfile.stem)
        frontmatter = f"""---
title: {title}
---

"""
        content = re.sub(r'^# .*\n', '', content, count=1)
        final_content = frontmatter + content.strip()
        target_path = target_dir / target_name
        target_path.write_text(final_content)
        print(f"  [✓] Synced: {srcfile.name} -> audit/{target_name}")
        count += 1

    print(f"  [✓] Synced {count} audit files")


def sync_site_docs():
    """Sync site-level docs from FRAMEWORK_ROOT/docs/lexigram-docs to CONTENT_ROOT.
    Only replaces files that already exist in the target (overlay, not add)."""
    src = FRAMEWORK_ROOT / "docs" / "lexigram-docs"
    if not src.exists():
        print(f"  [!] Site docs source not found at {src}")
        return

    skip_dirs = {"audit", "reference"}
    count = 0
    for srcfile in src.rglob("*"):
        if not srcfile.is_file():
            continue
        rel = srcfile.relative_to(src)
        if rel.parts and rel.parts[0] in skip_dirs:
            continue
        tgt = CONTENT_ROOT / rel
        tgt.parent.mkdir(parents=True, exist_ok=True)
        tgt.write_bytes(srcfile.read_bytes())
        count += 1
    print(f"  [✓] Synced site docs: {count} files copied")


if __name__ == "__main__":
    sync_readmes()
    sync_error_codes()
    sync_cli_commands()
    sync_env_vars()
    sync_audit_files()
    sync_site_docs()
