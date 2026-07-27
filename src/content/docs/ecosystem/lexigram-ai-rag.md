---
title: "lexigram-ai-rag"
description: "Retrieval-Augmented Generation pipeline — chunking, retrieval, synthesis, and citation."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-rag` provides a configurable RAG pipeline with pluggable chunking strategies, retrieval backends, reranking, context compression, HyDE (Hypothetical Document Embeddings), and answer synthesis.

## Installation

```bash
pip install lexigram-ai-rag
```

## Quick Start

```python
from lexigram.ai.rag import RAGModule
from lexigram.ai.rag.config import RAGConfig

module = RAGModule.configure(RAGConfig(chunk_size=512))
```

## Key Features

- Chunking: fixed-size, semantic, recursive, and code-aware strategies
- Retrieval strategies with multi-source fusion and reranking
- Built-in HyDE, context compression, and citation generation
- Pipeline builder for composing custom retrieval-synthesis flows

## Configuration

`RAGConfig` accepts `chunk_size`, `chunk_overlap`, retrieval and synthesis sub-configs. The `PipelineBuilder` lets you compose custom pipeline stages.

## Related

- [Guide](/guides/ai-rag/)
- [Vector Stores](/ecosystem/lexigram-vector/)
