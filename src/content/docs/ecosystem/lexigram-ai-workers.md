---
title: "lexigram-ai-workers"
description: "Background AI workers for batch embedding, document ingestion, maintenance, and dead-letter queue recovery."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-workers` provides background processing for AI workloads — batch embedding generation, document ingestion pipelines, scheduled maintenance tasks, and a dead-letter queue with error classification and retry logic.

## Installation

```bash
pip install lexigram-ai-workers
```

## Quick Start

```python
from lexigram.ai.workers import WorkersModule
from lexigram.ai.workers.config import WorkersConfig

module = WorkersModule.configure(
    WorkersConfig(max_retries=3),
    enable_scheduler=True,
)
```

## Key Features

- Document ingestion workers with progress tracking
- Batch embedding workers for vector store population
- Maintenance workers for scheduled cleanup and health checks
- Dead-letter queue with error classification and automated retry

## Configuration

`WorkersConfig` accepts `max_retries`, `task_timeout`, `check_interval`, and `base_backoff`. The scheduler is enabled by default; disable it for worker-only processes.

## Related

- [Guide](/guides/ai-workers/)
- [Vector](/ecosystem/lexigram-vector/)
