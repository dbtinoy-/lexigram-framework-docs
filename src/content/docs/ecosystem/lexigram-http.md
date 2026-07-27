---
title: "lexigram-http"
description: "Outbound HTTP client — connection pooling, resilience, interceptors, and typed request/response contexts."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Async outbound HTTP client with connection pooling, retry, circuit breaker, and interceptor chains. Designed for service-to-service communication within the DI container.

## Installation

```bash
pip install lexigram-http
```

## Quick Start

```python
from lexigram.http import HTTPModule, HTTPClient

@module(imports=[HTTPModule.configure()])
class AppModule(Module):
    pass

# Later, resolve from container
client = await container.resolve(HTTPClient)
response = await client.get("https://api.example.com/health")
```

## Key Features

- Connection pooling via `ConnectionPool`
- Retry with exponential backoff and circuit breaker
- Interceptor chain for request/response transformation
- Typed `RequestContext` and `ResponseContext`
- Base URL client for API-specific clients
- Streaming response support

## Configuration

`HTTPClientConfig` manages timeout, pooling, retry policy, and circuit breaker thresholds.

## Related

- [Guide](/guides/http-client/)
- [`lexigram-web`](/ecosystem/lexigram-web/) — inbound HTTP server
