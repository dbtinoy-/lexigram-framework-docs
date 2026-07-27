---
title: "lexigram-graph"
description: "Graph databases — Neo4j and in-memory backends, node/edge modeling, traversal, and Cypher query execution."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Graph database support with Neo4j and in-memory backends. Provides node/edge modeling, Cypher query execution, graph traversal, and event hooks.

## Installation

```bash
pip install lexigram-graph[neo4j]
```

Extras: `[neo4j]`.

## Quick Start

```python
from lexigram.graph import GraphModule, GraphConfig

@module(imports=[
    GraphModule.configure(GraphConfig(uri="bolt://localhost:7687"))
])
class AppModule(Module):
    pass
```

## Key Features

- Neo4j backend with `Neo4jGraphStore` and `Neo4jGraph`
- In-memory graph store for testing
- `GraphStoreProtocol` and `GraphProtocol` from contracts
- Cypher query execution and result mapping
- Node/edge lifecycle events
- Base classes for custom graph implementations

## Configuration

`GraphConfig` manages connection URI, credentials, and pool settings. `Neo4jConfig` for Neo4j-specific options.

## Related

- [Guide](/guides/graph-databases/)
- [`lexigram-nosql`](/ecosystem/lexigram-nosql/) — document database support
