---
title: "lexigram-ai-observability"
description: "AI-specific tracing, metrics, health monitoring, and callback management for LLM and vector operations."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-observability` adds AI-domain observability on top of `lexigram-monitor` — tracing for LLM calls and vector operations, AI-specific health checks (provider latency, quota usage), and metrics for token consumption and error rates.

## Installation

```bash
pip install lexigram-ai-observability
```

## Quick Start

```python
from lexigram.ai.observability import ObservabilityModule

module = ObservabilityModule.configure()
```

## Key Features

- Decorator-based tracing: `@trace_llm`, `@trace_rag`, `@trace_vector`
- AI health monitor with per-provider health checks
- Wrappers: `ObservableLLMClient`, `ObservableVectorStore`
- Callback manager for custom instrumentation hooks

## Configuration

`ObservabilityConfig` accepts exporter settings, sampling rate, and health check intervals. Exports `AITracerProtocol` for injection.

## Related

- [Guide](/guides/ai-observability/)
- [Monitoring](/ecosystem/lexigram-monitor/)
- [Feedback](/ecosystem/lexigram-ai-feedback/)
