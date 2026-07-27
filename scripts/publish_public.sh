#!/usr/bin/env bash
# Build (and optionally push) the PUBLIC docs site mirror.
#
#   ./scripts/publish_public.sh                  # DRY RUN — build + verify, no push
#   ./scripts/publish_public.sh --push           # Incremental push (preserves history)
#   ./scripts/publish_public.sh --reset --push   # Force-push fresh single-commit reset
#
# Override: STAGE (temp dir), PUBLIC_REMOTE, COMMIT_MSG.
set -euo pipefail
export GIT_EDITOR=true
cd "$(dirname "$0")/.."
REPO_ROOT="$(pwd)"

RESET=0; PUSH=0
for arg in "$@"; do
  [ "$arg" = "--reset" ] && RESET=1
  [ "$arg" = "--push" ]  && PUSH=1
done
STAGE="${STAGE:-$(mktemp -d)/lexigram-docs}"
PUBLIC_REMOTE="${PUBLIC_REMOTE:-git@github.com:dbtinoy-/lexigram-framework-docsework-docs.git}"
if [ -z "${COMMIT_MSG:-}" ]; then
  echo "ERROR: COMMIT_MSG is required. Usage: COMMIT_MSG=\"your message\" $0 [--push]"
  exit 1
fi

# Proprietary packages — must never appear in public output.
PROPRIETARY_RE='lexigram-ai-guard|lexigram-ai-governance|lexigram-ai-evaluation|lexigram-ai-prompt'
# Internal hostnames / domains — must be replaced before publish.
INTERNAL_RE='analytics\.internal'

echo "== staging at: $STAGE =="
rm -rf "$STAGE"
mkdir -p "$STAGE"

# ── Generate docs from framework source first ────────────────────────────────
echo "== generating docs =="
python3 scripts/sync-readmes.py
python3 scripts/generate-api.py

# ── Copy repo content (git-tracked files only) ────────────────────────────────
echo "== copying tracked content =="
git ls-files --cached --others --exclude-standard | while read -r f; do
  mkdir -p "$STAGE/$(dirname "$f")"
  cp "$f" "$STAGE/$f"
done

# Copy untracked-but-needed artifacts (e.g., public/ files not yet staged)
if [ -d public ]; then
  mkdir -p "$STAGE/public"
  cp -r public/* "$STAGE/public/" 2>/dev/null || true
fi

# ── SANITIZE: Remove proprietary package references ──────────────────────────

# 1. _redirects — remove redirects for proprietary packages
echo "== sanitizing _redirects =="
if [ -f "$STAGE/public/_redirects" ]; then
  grep -v -E "$PROPRIETARY_RE" "$STAGE/public/_redirects" > "$STAGE/public/_redirects.clean"
  mv "$STAGE/public/_redirects.clean" "$STAGE/public/_redirects"
  # Also remove /admin /utilities/admin redirects pointing to lexigram-admin
  grep -v -E '^/(admin|utilities/admin)' "$STAGE/public/_redirects" > "$STAGE/public/_redirects.clean"
  mv "$STAGE/public/_redirects.clean" "$STAGE/public/_redirects"
fi

# 2. scripts/anchored-summary.md — internal process notes, not for public
echo "== sanitizing anchored-summary.md =="
if [ -f "$STAGE/scripts/anchored-summary.md" ]; then
  rm "$STAGE/scripts/anchored-summary.md"
fi

# 3. Internal hostnames in docs
echo "== sanitizing internal hostnames =="
for f in "$STAGE/src/content/docs/guides/ai-mcp.md" \
         "$STAGE/src/content/docs/platform/lexigram-ai-mcp/api.md"; do
  if [ -f "$f" ]; then
    sed -i "s/$INTERNAL_RE/example.internal/g" "$f"
  fi
done

# 4. Reference CLI — remove lexigram-admin row
echo "== sanitizing reference/cli.md =="
CLI_MD="$STAGE/src/content/docs/reference/cli.md"
if [ -f "$CLI_MD" ]; then
  grep -v "lexigram-admin" "$CLI_MD" > "$CLI_MD.clean" && mv "$CLI_MD.clean" "$CLI_MD"
fi

# 5. Reference errors — remove LEX_ERR_ADMIN_001 row
echo "== sanitizing reference/errors.md =="
ERR_MD="$STAGE/src/content/docs/reference/errors.md"
if [ -f "$ERR_MD" ]; then
  grep -v "LEX_ERR_ADMIN" "$ERR_MD" > "$ERR_MD.clean" && mv "$ERR_MD.clean" "$ERR_MD"
fi

# 6. Sidebar — remove lexigram-admin label
echo "== sanitizing Sidebar.astro =="
SIDEBAR="$STAGE/src/components/starlight/Sidebar.astro"
if [ -f "$SIDEBAR" ]; then
  grep -v "'lexigram-admin'" "$SIDEBAR" > "$SIDEBAR.clean" && mv "$SIDEBAR.clean" "$SIDEBAR"
fi

# 7. NARRATIVE_SPINE — remove private project mention
echo "== sanitizing NARRATIVE_SPINE.md =="
SPINE="$STAGE/NARRATIVE_SPINE.md"
if [ -f "$SPINE" ]; then
  grep -v "private project" "$SPINE" > "$SPINE.clean" && mv "$SPINE.clean" "$SPINE"
fi

# 8. Package docs — sanitize lexigram-admin mentions
echo "== sanitizing package docs =="
# lexigram-testing/api.md
TESTING_API="$STAGE/src/content/docs/packages/utilities/lexigram-testing/api.md"
if [ -f "$TESTING_API" ]; then
  sed -i 's/for lexigram-admin endpoints/for admin panel endpoints/g' "$TESTING_API"
fi
# lexigram-ui/api.md
UI_API="$STAGE/src/content/docs/packages/web/lexigram-ui/api.md"
if [ -f "$UI_API" ]; then
  sed -i 's/Base UI Component for lexigram-admin (HTPy-backed)/Base UI Component for admin panel (HTPy-backed)/g' "$UI_API"
fi

# 9. Architecture diagrams — sanitize lexigram-admin references
ARCH_CONTRACTS="$STAGE/src/content/docs/packages/foundation/lexigram-contracts/docs/ARCHITECTURE.md"
if [ -f "$ARCH_CONTRACTS" ]; then
  sed -i 's/lexigram-admin //g' "$ARCH_CONTRACTS"
  sed -i 's/ lexigram-admin//g' "$ARCH_CONTRACTS"
fi
ARCH_WEBHOOK="$STAGE/src/content/docs/packages/web/lexigram-webhook/docs/ARCHITECTURE.md"
if [ -f "$ARCH_WEBHOOK" ]; then
  sed -i '/Admin\[lexigram-admin/,+3 d' "$ARCH_WEBHOOK"
  # Remove orphaned arrow lines if mermaid breaks
  sed -i '/Admin -->/d' "$ARCH_WEBHOOK"
fi

# 10. Remove internal docs/ directory (specs, process docs)
echo "== removing internal docs/ =="
rm -rf "$STAGE/docs"

# 11. Remove dev scripts — they contain proprietary package references and serve
#     no purpose in the public mirror (they generate docs from the framework monorepo).
echo "== removing dev scripts =="
rm -f "$STAGE/scripts/sync-readmes.py"
rm -f "$STAGE/scripts/generate-api.py"
find "$STAGE/scripts" -name "anchored-summary.md" -delete 2>/dev/null || true
find "$STAGE/scripts" -name "*.log" -delete 2>/dev/null || true

# ── LEAK GUARD ────────────────────────────────────────────────────────────────
echo "== verifying no proprietary leaks =="
if grep -rilE "$PROPRIETARY_RE" "$STAGE" --include="*.md" --include="*.astro" --include="*_redirects" --include="*.py" 2>/dev/null | grep -v node_modules | head -20; then
  echo "ERROR: proprietary package names leaked in staged files (see above)"
  exit 1
fi
if grep -rilE "$INTERNAL_RE" "$STAGE" --include="*.md" --include="*.astro" 2>/dev/null | grep -v node_modules | head -10; then
  echo "ERROR: internal hostnames leaked in staged files (see above)"
  exit 1
fi
if grep -rilE "private project" "$STAGE/NARRATIVE_SPINE.md" 2>/dev/null; then
  echo "ERROR: private project reference still in NARRATIVE_SPINE.md"
  exit 1
fi
echo "  clean: no proprietary leaks."

# ── Init git and commit ──────────────────────────────────────────────────────
cd "$STAGE"

if [ "$RESET" = "1" ]; then
  git init -q -b main
  git add -A
  git commit -q -m "Initial public release — Lexigram (MIT)"
  echo "== fresh history (reset) =="
  git log --oneline
else
  git init -q -b main
  git add -A
  if git diff --cached --quiet; then
    echo "== no changes to commit =="
  else
    git commit -q -m "$COMMIT_MSG"
    echo "== committed =="
    git log --oneline -5
  fi
fi

# Leak check in git history
if git log --all --name-only --pretty=format: | sort -u | grep -qiE "$PROPRIETARY_RE"; then
  echo "ERROR: proprietary package path found in git history"; exit 1
fi
echo "  clean history."

# ── Push ──────────────────────────────────────────────────────────────────────
if [ "$PUSH" = "1" ]; then
  if git remote get-url origin &>/dev/null; then
    git remote set-url origin "$PUBLIC_REMOTE"
  else
    git remote add origin "$PUBLIC_REMOTE"
  fi
  if [ "$RESET" = "1" ]; then
    git push --force -u origin main
    echo "PUSHED (force reset) to $PUBLIC_REMOTE"
  else
    git push -u origin main
    echo "PUSHED (incremental) to $PUBLIC_REMOTE"
  fi
else
  echo ""
  echo "DRY RUN complete — verified, no push. Inspect: $STAGE"
  echo "To publish: COMMIT_MSG=\"msg\" ./scripts/publish_public.sh --push"
  echo "To reset history: COMMIT_MSG=\"msg\" ./scripts/publish_public.sh --reset --push"
fi
