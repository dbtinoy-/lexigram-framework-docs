---
title: "lexigram-graphql"
description: "Strawberry-based GraphQL — schema building, execution, subscriptions, depth/complexity guards, and persisted queries."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Full-featured GraphQL support using Strawberry. Includes schema building, query execution, subscriptions via WebSocket, depth-limit and complexity analysis, persisted queries (APQ), and DataLoader integration.

## Installation

```bash
pip install lexigram-graphql
```

## Quick Start

```python
import strawberry
from lexigram.graphql import GraphQLModule

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"

app.add_module(GraphQLModule.configure(query_class=Query, endpoint="/graphql"))
```

## Key Features

- Strawberry schema building with `create_schema` builder
- Subscriptions with WebSocket transport
- Depth and alias limit guards
- Query complexity analysis
- Persisted queries (APQ) with `PersistedQueryStore`
- DataLoader protocol for N+1 prevention
- Tracing and metrics extensions

## Configuration

`GraphQLConfig` manages introspection, playground, subscriptions, depth limits, caching, and tracing settings.

## Related

- [Guide](/guides/graphql/)
- [`lexigram-web`](/ecosystem/lexigram-web/) — web server integration
