---
title: "lexigram-ai-memory"
description: "Three-tier AI memory system — working, episodic, and semantic memory with pluggable backends."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-memory` implements a three-tier memory architecture: working memory (conversation buffers, token-budget allocation), episodic memory (event logs with compression), and semantic memory (entity extraction, fact stores, consolidation).

## Installation

```bash
pip install lexigram-ai-memory
```

## Quick Start

```python
from lexigram.ai.memory import MemoryModule
from lexigram.ai.memory.config import MemoryConfig

module = MemoryModule.configure(
    MemoryConfig(backend="in_memory"),
    enable_consolidation=True,
)
```

## Key Features

- Working memory: conversation buffers, token budget allocator, context pruning
- Episodic memory: store, compress, and retrieve event histories
- Semantic memory: entity extraction, fact stores, knowledge graphs
- Consolidation scheduler with recency-decay and deduplication strategies

## Configuration

`MemoryConfig` accepts per-tier configs (`working`, `episodic`, `semantic`), backend selection, and consolidation intervals.

## Related

- [Guide](/guides/ai-memory/)
- [Sessions](/ecosystem/lexigram-ai-session/)
