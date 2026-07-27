---
title: "lexigram-testing"
description: "Fakes, test clients/beds, protocol compliance suites, and a deterministic clock for fast, isolated tests."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Speed up tests with in-memory fakes (`FakeCache`, `FakeEventBus`, `FakeAuditLogger`, etc.), test beds for web/DB/AI/tasks, and compliance suites that verify protocol implementations behave correctly.

## Installation

```bash
pip install lexigram-testing
```

## Quick Start

```python
from lexigram.testing import (
    WebTestClient,
    DatabaseTestBed,
    FixedClock,
    FakeCache,
)

clock = FixedClock("2026-01-01")
client = WebTestClient(app)
```

## Key Features

- Fakes: `FakeCache`, `FakeEventBus`, `FakeCommandBus`, `FakeAuditLogger`, `FakeTracer`, etc.
- Test beds: `WebTestBed`, `DatabaseTestBed`, `AITestBed`, `TaskTestBed`
- Test clients: `WebTestClient`, `DatabaseTestClient`, `TaskTestClient`
- Compliance suites: `CacheBackendCompliance`, `QueueBackendCompliance`, `VectorStoreCompliance`, etc.
- `FixedClock` for deterministic time in tests
- `TestingModule.configure()` for DI integration

## Configuration

`TestingModule` registers no providers by default — it is a marker module for test environment setup.

## Related

- [Guide](/guides/testing/)
- All ecosystem packages — each has a compliance suite
