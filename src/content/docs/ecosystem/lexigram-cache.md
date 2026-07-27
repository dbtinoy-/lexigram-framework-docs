---
title: "lexigram-cache"
description: "Multi-backend caching — Redis, Memcached, and in-memory backends with stampede protection and serialization."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Unified caching API across multiple backends. Provides `CacheService` for DI injection, stampede protection, configurable serialization (JSON, Pickle, compressed), and request-scoped caching.

## Installation

```bash
pip install lexigram-cache[redis]
```

Extras: `[redis]`, `[memcached]`, `[semantic]`.

## Quick Start

```python
from lexigram.cache import CacheModule, CacheConfig, BackendType

@module(imports=[
    CacheModule.configure(CacheConfig(backend=BackendType.REDIS))
])
class AppModule(Module):
    pass

# Resolve CacheService from the container
cache = await container.resolve(CacheService)
await cache.set("key", {"data": "value"}, ttl=300)
```

## Key Features

- Pluggable backends: Redis, Memcached, in-memory
- Stampede protection with `CacheProtectionStrategyProtocol`
- Decorator-based caching (`@cacheable`, `@cache`, `@remember`)
- Request-scoped cache (`cache_in_request`)
- JSON, Pickle, and compressing serializers
- Cache stats, metrics, and health checks

## Configuration

`CacheConfig` manages backend type, connection settings, TTL defaults, serialization, and stampede protection settings.

## Related

- [Guide](/guides/caching/)
- [`lexigram-storage`](/ecosystem/lexigram-storage/) — blob and KV storage
