---
title: "lexigram-contracts"
description: "Zero-dependency protocols, shared types, base exceptions, and cross-package enums for the Lexigram ecosystem."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-contracts` is the shared contract layer of the framework. It defines protocols, value types, base exceptions, and enums that all other packages depend on. It has zero runtime dependencies.

## Installation

```bash
pip install lexigram-contracts
```

This is a dependency-only package — other packages re-export from it. You typically import from `lexigram` or the specific extension package rather than directly from `lexigram.contracts`.

Key exports include `CacheBackendProtocol`, `DatabaseProviderProtocol`, `LLMClientProtocol`, `ContainerProtocol`, `ConfigProtocol`, `BlobStoreProtocol`, `CommandBusProtocol`, `RepositoryProtocol`, `ChatMessage`, `DomainEvent`, `LexigramError`, and many more — all re-exported from the respective extension packages for convenience.

## Key Features

- Service boundary protocols (`CacheBackendProtocol`, `DatabaseProviderProtocol`, `LLMClientProtocol`, etc.)
- Shared value types (`ChatMessage`, `DomainEvent`, `HealthCheckResult`, etc.)
- Base exception hierarchy (`LexigramError` → `DomainError`, `InfrastructureError`, etc.)
- Cross-package enums (`Role`, `HealthStatus`, `SQLDialect`, etc.)
- Domain building blocks (`AggregateRootProtocol`, `SpecificationProtocol`, `CursorPage`)
- Infrastructure abstractions (`BlobStoreProtocol`, `SecretStoreProtocol`, `StateStoreProtocol`)

## Exception Hierarchy

```
LexigramError
├── DomainError           (domain rule violations)
├── InfrastructureError   (connection, I/O failures)
├── ContainerError        (DI container failures)
├── SecurityError         (auth, guard violations)
├── AIError               (LLM, RAG, memory errors)
├── AgentError            (agent execution failures)
├── ResilienceError       (circuit breaker, retry)
└── EventError            (event bus failures)
```

All extension packages extend these base exceptions.

## Related

- [Guide](/guides/contracts/)
- [`lexigram`](/ecosystem/foundation/) — core framework
