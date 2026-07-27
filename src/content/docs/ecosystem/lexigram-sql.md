---
title: "lexigram-sql"
description: "Async SQL — repository pattern, GenericRepository, migrations, query builder, and unit of work."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Async-first SQL integration with support for PostgreSQL, MySQL, and SQLite. Implements the repository pattern with `GenericRepository`, type-safe query building, migration management, and unit-of-work transactions.

## Installation

```bash
pip install lexigram-sql[postgres]
```

Extras: `[postgres]`, `[mysql]`, `[sqlite]`.

## Quick Start

```python
from lexigram.sql import DatabaseModule, DatabaseConfig, GenericRepository

@module(imports=[
    DatabaseModule.configure(DatabaseConfig(url="postgresql+asyncpg://..."))
])
class AppModule(Module):
    pass

# Then inject GenericRepository[User]
```

## Key Features

- `GenericRepository` with CRUD, filtering, and pagination
- `AsyncQueryBuilder` for type-safe SQL construction
- Migration management with `SimpleMigrationManager`
- Unit of work with `SimpleUnitOfWork` and `transaction`
- Row-level security policies
- Full-text search across dialects (`PostgresFTSQuery`, `MySQLFTSQuery`)
- Auditing via `AuditRepositoryMixin`

## Configuration

`DatabaseConfig` manages connection URL, pool size, migration paths, and dialect-specific settings.

## Related

- [Guide](/guides/database/)
- [`lexigram-nosql`](/ecosystem/lexigram-nosql/) — document database support
