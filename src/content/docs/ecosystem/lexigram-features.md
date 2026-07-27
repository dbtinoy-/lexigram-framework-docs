---
title: "lexigram-features"
description: "Feature flags with TTL caching, targeting rules, A/B variant support, and pluggable providers."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Toggle features at runtime with `FlagManager` and `FlagProviderProtocol`. Supports boolean and multi-variant flags with percentage rollouts and user-list targeting. Decorators for gating async and sync code paths.

## Installation

```bash
pip install lexigram-features
```

## Quick Start

```python
from lexigram.features.module import FeatureFlagsModule
from lexigram.features.config import FeatureFlagsConfig

app.add_module(FeatureFlagsModule.configure(
    FeatureFlagsConfig(initial_flags={"beta_feature": True})
))
```

```python
from lexigram.features import feature_flag

@feature_flag("beta_feature")
async def new_feature(): ...
```

## Key Features

- Flag types: boolean, percentage, user-list, and custom targeting
- Backends: local, environment, chained, cache-backed (`CacheBackendFlagProvider`)
- `FlagManager` with TTL caching, overrides, change listeners
- Decorators: `feature_flag`, `feature_flag_sync`, `require_flag`, `require_flag_sync`

## Configuration

`FeatureFlagsModule.configure()` accepts a `FeatureFlagsConfig` with initial flags and provider configuration.

## Related

- [Guide](/guides/feature-flags/)
- [`lexigram-cache`](/ecosystem/lexigram-cache/) — cache-backed flag provider
