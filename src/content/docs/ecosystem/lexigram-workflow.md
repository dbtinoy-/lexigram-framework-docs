---
title: "lexigram-workflow"
description: "Workflow orchestration — pipelines, sagas, bulk operations, and a directed-graph execution engine."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Compose and execute multi-step workflows. Use `Pipeline` with `FunctionStep`, `ConditionalStep`, and `ParallelStep`. Coordinate distributed sagas with `AbstractSaga`. Run directed acyclic graphs via `WorkflowEngine` and `WorkflowBuilder`.

## Installation

```bash
pip install lexigram-workflow
```

## Quick Start

```python
from lexigram.workflow.module import WorkflowModule

app.add_module(WorkflowModule.configure())
```

## Key Features

- Pipeline orchestration with steps, conditionals, and parallel branches
- Saga state machines with compensation (`AbstractSaga`, `saga_step`)
- Directed-graph engine (`WorkflowEngine`, `WorkflowBuilder`, `WorkflowRunner`)
- Graph node types: `LLMNode`, `AgentNode`, `ToolNode`, `HumanNode`, `GateNode`
- Workflow checkpointing, execution history, and versioning

## Configuration

Optional `BulkOperationConfig` and `SagaStoreProtocol`. Defaults to in-memory state store.

## Related

- [Guide](/guides/workflows/)
- [`lexigram-tasks`](/ecosystem/lexigram-tasks/) — background task scheduling
