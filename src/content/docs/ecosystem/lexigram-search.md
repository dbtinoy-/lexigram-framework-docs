---
title: "lexigram-search"
description: "Full-text search — Meilisearch, Elasticsearch, Typesense, and SQL FTS backends with faceting, filtering, and bulk indexing."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Unified search abstraction supporting Meilisearch, Elasticsearch, Typesense, Algolia, and database-native full-text search. Provides faceted filtering, bulk indexing, suggestions, and query validation.

## Installation

```bash
pip install lexigram-search[meilisearch]
```

Extras: `[elasticsearch]`, `[meilisearch]`, `[algolia]`, `[postgres]`, `[mysql]`.

## Quick Start

```python
from lexigram.search import SearchModule, SearchConfig, BackendType

@module(imports=[
    SearchModule.configure(SearchConfig(backend=BackendType.MEILISEARCH))
])
class AppModule(Module):
    pass

# Resolve SearchEngine from the container
engine = await container.resolve(SearchEngine)
results = await engine.search("query")
```

## Key Features

- Multiple backend support via `SearchEngine` and `FederatedSearchEngine`
- `FilterSet` with typed filter conditions and operators
- Faceted search and aggregation
- Bulk indexing via `SearchEntityRepository`
- Suggestion engine for autocomplete
- Query validation and sanitization
- Search analytics recording

## Configuration

`SearchConfig` manages backend type, connection URL, API keys, index settings, and timeouts.

## Related

- [Guide](/guides/search/)
- [`lexigram-sql`](/ecosystem/lexigram-sql/) — SQL FTS integration
