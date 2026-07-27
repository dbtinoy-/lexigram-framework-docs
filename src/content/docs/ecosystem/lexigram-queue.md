---
title: "lexigram-queue"
description: "Message bus / queue with named multi-backend support (Redis, RabbitMQ, Kafka, SQS, GCP Pub/Sub, Azure Service Bus)."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Async message bus with named DI support. Publish and consume through an abstract `QueueProtocol` while the container selects the right backend. Includes transactional outbox, dead-letter queue, and a middleware pipeline.

## Installation

```bash
pip install lexigram-queue
```

## Quick Start

```python
from lexigram.queue.config import QueueConfig
from lexigram.queue.module import QueueModule

app.add_module(QueueModule.configure(QueueConfig(backends=[...])))
app.add_module(QueueModule.scope(OrderConsumer, PaymentConsumer))
```

## Key Features

- Multi-backend queues (memory, Redis, RabbitMQ, Kafka, SQS, GCP Pub/Sub, Azure Service Bus)
- Named injection for multiple named queue connections
- Transactional outbox and dead-letter queue
- Middleware pipeline via `MessagePipeline` and `MiddlewareBase`
- Consumer scoping via `QueueModule.scope()`

## Configuration

Provide a `QueueConfig` with backend definitions. Resolve `QueueProtocol` via container — the primary and named queues are selected by the DI layer.

## Related

- [Guide](/guides/queue/)
- [`lexigram-tasks`](/ecosystem/lexigram-tasks/) — background task workers on top of queues
