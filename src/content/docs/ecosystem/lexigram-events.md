---
title: "lexigram-events"
description: "CQRS and event sourcing — commands/events/queries, event store, projections, sagas, and stream processing."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Complete CQRS and event sourcing implementation. Provides command, event, and query buses; event stores (PostgreSQL, MongoDB, Redis, in-memory); aggregate roots; projections; sagas; and message streaming.

## Installation

```bash
pip install lexigram-events[postgres]
```

Extras: `[postgres]`, `[sqlite]`, `[mongo]`, `[rabbitmq]`.

## Quick Start

```python
from lexigram.events import (
    EventsModule, EventsConfig, CommandBusImpl, AggregateRoot
)
from lexigram.contracts.domain import DomainEvent

class UserCreated(DomainEvent):
    user_id: str
    name: str

app.add_module(EventsModule.configure(EventsConfig()))
```

## Key Features

- `CommandBusImpl`, `EventBusImpl`, `QueryBusImpl` with middleware pipeline
- Event stores: Postgres, MongoDB, Redis, SQLite, in-memory
- `AggregateRoot`, `Entity`, `ValueObject` for DDD
- `EventSourcingRepository` for aggregate persistence
- Projections for building read models
- Sagas for long-running business processes
- Webhook dispatch and message broker adapters

## Configuration

`EventsConfig` manages bus settings, event store backend, snapshot strategy, and middleware configuration.

## Related

- [Guide](/guides/event-driven/)
- [`lexigram-queue`](/ecosystem/lexigram-queue/) — message queue integration
