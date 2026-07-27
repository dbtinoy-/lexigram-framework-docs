---
title: "lexigram-ai-feedback"
description: "Feedback collection and processing pipeline for AI responses with pluggable storage and middleware."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-feedback` provides a complete feedback loop for AI systems — collect, validate, process, and store feedback on AI responses. Includes middleware for automatic capture, a collector service, and pluggable storage backends.

## Installation

```bash
pip install lexigram-ai-feedback
```

## Quick Start

```python
from lexigram.ai.feedback import FeedbackModule
from lexigram.ai.feedback.config import FeedbackConfig

module = FeedbackModule.configure(
    FeedbackConfig(storage="database")
)
```

## Key Features

- Feedback collector and service layer with typed `FeedbackItem` and `FeedbackType`
- Pluggable stores: in-memory, database, cached (Redis)
- Middleware for automatic feedback capture in web/API contexts
- Processor pipeline with validation and enrichment hooks

## Configuration

`FeedbackConfig` accepts `storage` backend, processor settings, and middleware options. Supports `database`, `cache`, and `in_memory` backends.

## Related

- [Guide](/guides/ai-feedback/)
- [Observability](/ecosystem/lexigram-ai-observability/)
