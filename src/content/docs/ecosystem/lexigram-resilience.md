---
title: "lexigram-resilience"
description: "Fault-tolerance patterns — circuit breaker, retry, bulkhead, rate limiter, throttle, timeout, and idempotency."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Protect your services with configurable resilience policies. Wrap calls with `circuit_breaker`, `retry`, `bulkhead`, `throttle`, and `with_timeout` decorators. Compose policies via `ResiliencePipeline`.

## Installation

```bash
pip install lexigram-resilience
```

## Quick Start

```python
from lexigram.resilience.module import ResilienceModule

app.add_module(ResilienceModule.configure())
```

```python
from lexigram.resilience import retry, circuit_breaker

@retry(max_attempts=3)
@circuit_breaker(failure_threshold=5)
async def call_external_api(): ...
```

## Key Features

- `CircuitBreaker` with `CircuitBreakerRegistryProtocol` and distributed backends
- `RetryPolicy` with configurable delay, jitter, and max attempts
- `Bulkhead` for concurrent-execution limits
- `RateLimiter` and `Throttler` for throughput control
- `TimeoutManager` and `with_timeout` decorator
- Idempotency support (`idempotent` decorator, `IdempotencyStoreProtocol`)

## Configuration

Optional `ResilienceConfig`. All policies have sensible framework defaults.

## Related

- [Guide](/guides/resilience/)
- [`lexigram-monitor`](/ecosystem/lexigram-monitor/) — observability integration
