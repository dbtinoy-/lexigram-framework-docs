---
title: "lexigram-tenancy"
description: "Multi-tenant resolution, isolation strategies, lifecycle management, and config overrides."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Resolve tenants from headers, subdomains, or custom resolvers. Isolate data via schema-per-tenant, row-level, or database strategies. Provision and manage tenant lifecycles.

## Installation

```bash
pip install lexigram-tenancy
```

## Quick Start

```python
from lexigram.tenancy.module import TenancyModule
from lexigram.tenancy.config import TenancyConfig, ResolutionConfig

app.add_module(TenancyModule.configure(
    TenancyConfig(resolution=ResolutionConfig(resolvers=["header"]))
))
```

## Key Features

- Pluggable resolvers via `CompositeResolver` and `ResolverRegistry`
- Isolation strategies: schema, row-level, database
- Tenant lifecycle: provisioning, validation (`TenantValidator`)
- Config overrides per tenant via `TenantConfigService`
- `TenantContextMiddleware` for web request scoping

## Configuration

`TenancyModule.configure()` accepts a `TenancyConfig` with resolution, isolation, lifecycle, and integration settings.

## Related

- [Guide](/guides/tenancy/)
- [`lexigram-auth`](/ecosystem/lexigram-auth/) — per-tenant auth isolation
