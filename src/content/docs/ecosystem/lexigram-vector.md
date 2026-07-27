---
title: "lexigram-vector"
description: "Unified vector store abstraction with pluggable backends — pgvector, Qdrant, Pinecone, Chroma, Milvus, and in-memory."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-vector` provides a contract-based vector store abstraction with swappable backends, embedding integration, and collection management. Powers semantic search, RAG retrieval, and memory indexing.

## Installation

```bash
pip install lexigram-vector
```

## Quick Start

```python
from lexigram.vector.config import VectorConfig

config = VectorConfig(
    provider="pgvector",
    dimension=1536,
)
```

## Key Features

- Backends: pgvector, Qdrant, Pinecone, Chroma, Milvus, in-memory
- Collection management with schema and index configuration
- Embedding integration via `lexigram-ai-llm` or external providers
- Batch upsert, filtered search, and hybrid (dense + sparse) retrieval

## Configuration

`VectorConfig` accepts `provider`, connection settings, embedding dimension, and similarity metric. Backend-specific settings passed via `backend_options`.

## Related

- [Guide](/guides/vector-stores/)
- [RAG](/ecosystem/lexigram-ai-rag/)
- [Memory](/ecosystem/lexigram-ai-memory/)
