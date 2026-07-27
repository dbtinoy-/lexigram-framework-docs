---
title: "lexigram-tasks"
description: "Background task workers, cron scheduling, job queues, and task orchestration."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Process background tasks with pluggable backends (memory, Redis, RabbitMQ). Schedule recurring jobs with `CronExpression`, chain tasks with `TaskChain` / `TaskGroup` / `TaskChord`, and track progress with real-time `ProgressTracker`.

## Installation

```bash
pip install lexigram-tasks
```

## Quick Start

```python
from lexigram.tasks.module import TasksModule

app.add_module(TasksModule.configure(worker_count=4))
app.add_module(TasksModule.scope(SendEmailTask, GenerateReportTask))
```

## Key Features

- Multi-backend task queues (memory, Redis, RabbitMQ)
- Cron-based scheduling via `TaskScheduler` and `ScheduledWorker`
- Task workflows: chains, groups, chords, branches
- Dead-letter queue, result stores, progress tracking
- Middleware pipeline (logging, metrics, timeouts)

## Configuration

`TasksModule.configure()` accepts a `TaskQueueProtocol` instance, worker count, and scheduler toggle. Scope task handlers with `TasksModule.scope()`.

## Related

- [Guide](/guides/tasks/)
- [`lexigram-queue`](/ecosystem/lexigram-queue/) — underlying message bus
