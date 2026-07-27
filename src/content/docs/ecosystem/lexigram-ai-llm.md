---
title: "lexigram-ai-llm"
description: "Multi-provider LLM client with support for OpenAI, Anthropic, Gemini, Ollama, Groq, Mistral, Cohere, and OpenRouter."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-llm` is a unified LLM client layer with provider-specific adapters, multi-provider routing, rate limiting, response caching, structured output extraction, and token-based pricing.

## Installation

```bash
pip install lexigram-ai-llm
```

## Quick Start

```python
from lexigram.ai.llm import LLMModule
from lexigram.ai.llm.config import ClientConfig

module = LLMModule.configure(
    ClientConfig(provider="openai", model="gpt-4o")
)
```

## Key Features

- Providers: OpenAI, Anthropic, Gemini, Ollama, Groq, Mistral, Cohere, OpenRouter
- Multi-provider routing with failover, quota enforcement, and model selection
- Structured output extraction (JSON, Pydantic, Instructor)
- Response caching (Redis, in-memory), rate limiting, and content filtering

## Configuration

`ClientConfig` accepts `provider`, `model`, `api_key`, `temperature`, `max_tokens`, and more. The `LLMModule.configure(routing=LLMConfig(...))` variant enables the multi-provider router instead of a single client.

## Related

- [Guide](/guides/ai-integration/)
- [LLM Routing](/guides/ai-llm-routing/)
