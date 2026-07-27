---
title: "lexigram"
description: "Core framework package — DI container, application lifecycle, modules, providers, configuration, and the Result type."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

The `lexigram` package is the framework core. It provides the dependency injection container, application lifecycle management, module/provider system, configuration, and the `Result[T, E]` type for explicit error handling.

## Installation

```bash
pip install lexigram
```

## Quick Start

```python
from lexigram import Application, Module, Provider

app = Application()
app.add_module(MyModule.configure())
await app.run()
```

## Key Features

- Async DI container with scoped, singleton, and transient lifetimes
- Module/provider pattern for composable application assembly
- `Result[T, E]` type with `Ok`/`Err` variants and chaining helpers
- Hook system (`HookRegistry`) for lifecycle interception
- Configuration via `BaseConfig` and `ConfigProvider`
- Ambient clock, identity, and hashing capabilities

## Configuration

`LexigramConfig` and `BaseConfig` handle framework and application configuration. YAML, env, and dict sources supported.

## Related

- [Guide](/guides/core/)
- [`lexigram-contracts`](/ecosystem/lexigram-contracts/) — protocols and shared types
