---
title: "lexigram-ai"
description: "Orchestration layer that discovers and wires all AI subsystems via Python entry points."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai` is the top-level AI orchestration package. It discovers sub-packages (`lexigram-ai-llm`, `lexigram-ai-rag`, etc.) via `lexigram.ai.modules` entry points and wires them into a single `AIProviderProtocol` implementation.

## Installation

```bash
pip install lexigram-ai
```

## Quick Start

```python
from lexigram.ai.config import AIConfig
from lexigram.ai.module import AIModule

config = AIConfig(llm={"provider": "openai", "model": "gpt-4o"})
module = AIModule.configure(config)
```

## Key Features

- Entry-point-based AI subsystem discovery — install sub-packages and they auto-register
- Unified `AIConfig` that nests LLM, RAG, vector, governance, and observability settings
- Lazy imports — sub-packages are loaded only when accessed

## Configuration

`AIConfig` reads from `LEX_AI__*` environment variables by default. Supports `llm`, `rag`, `vector`, `governance`, and `observability` sub-configs, plus a `subsystems` dict for third-party extensions.

## Related

- [Guide](/guides/ai-integration/)
- [Architecture](/fundamentals/architecture/)
