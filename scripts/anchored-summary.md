# Anchored Summary

## Goal
Enrich all 44 package ARCHITECTURE.md files with Mermaid diagrams and full section structure, fix docs site sidebar/TOC issues, and publish.

## Progress

### Done
- **ARCHITECTURE.md enrichment**: All 44 files processed across 8 tiers using parallel agents. **14,499 total lines, 195 Mermaid diagrams** (was ~6,260 lines, 6 diagrams).
- **Secret-IP leak fixed**: Removed `lexigram-ai-guard`/`governance`/`evaluation`/`prompt` from `lexigram-ai/docs/ARCHITECTURE.md` to pass publish verification.
- **Published to public mirror**: `8ff715f` pushed to `github.com/dbtinoy-/lexigram.git`.
- **Sidebar mini-mode fix** (`Head.astro:24-27`): First-visit default changed from `'true'` (mini) to expanded — `localStorage.getItem('sidebar-mini')` null no longer treated as `'true'`.
- **TOC on docs pages** (`TableOfContents.astro`): `ApiExplorer` no longer replaces the default Starlight Table of Contents for URLs containing `/docs/`.
- **Force right sidebar panel** (`PageSidebar.astro`): New override — always renders the right sidebar for `/docs/` pages regardless of `Astro.locals.starlightRoute.toc` state.

### In Progress
- (none)

### Blocked
- (none)

## Key Decisions
- ARCHITECTURE.md enrichment uses parallel subagents per tier — 3-8 files rewritten simultaneously.
- Each file gets 4-8 Mermaid diagrams (system role, provider lifecycle, data flow, exception hierarchy, extension points).
- Secret-IP package names removed from public `lexigram-ai` ARCHITECTURE.md to pass publish verification.
- `PageSidebar.astro` overrides Starlight's conditional TOC rendering — `/docs/` pages always show the right sidebar.

## Relevant Files
- `src/components/starlight/Head.astro`: Sidebar mini-mode default (`savedMini === null` no longer sets `'true'`).
- `src/components/starlight/TableOfContents.astro`: Guards `ApiExplorer` behind `!isSubDoc` block.
- `src/components/starlight/PageSidebar.astro`: Forces right sidebar panel on `/docs/` pages.
- `astro.config.mjs`: Registers PageSidebar component override.
