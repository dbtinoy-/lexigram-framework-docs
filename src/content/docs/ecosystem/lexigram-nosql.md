---
title: "lexigram-nosql"
description: "NoSQL document stores — MongoDB and DynamoDB backends, query builder, aggregation pipelines, and schema migration."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Document database support for MongoDB and DynamoDB. Provides a `DocumentStoreProtocol` abstraction, type-safe query builder, aggregation pipeline, and schema migration system.

## Installation

```bash
pip install lexigram-nosql[mongodb]
```

Extras: `[mongodb]`, `[dynamodb]`.

## Quick Start

```python
from lexigram.nosql import NoSQLModule, NoSQLConfig

@module(imports=[
    NoSQLModule.configure(NoSQLConfig(mongodb_url="mongodb://localhost:27017"))
])
class AppModule(Module):
    pass
```

## Key Features

- MongoDB and DynamoDB backends via `NoSQLProvider`
- `DocumentQueryBuilder` for type-safe query construction
- `AggregationPipeline` with MongoDB aggregation stages
- Schema migration manager with `MigrationManager`
- Comparison, logical, and update operators
- Collection-level migration operations

## Configuration

`NoSQLConfig` with `MongoDBConfig` and `DynamoDBConfig` for connection strings, credentials, and pool settings.

## Related

- [Guide](/guides/nosql/)
- [`lexigram-sql`](/ecosystem/lexigram-sql/) — relational database support
