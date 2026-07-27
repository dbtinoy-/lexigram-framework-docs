---
title: "lexigram-monitor"
description: "Observability — health checks, metrics, distributed tracing, structured logging, and profiling."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Collect metrics (counter, gauge, histogram, summary), emit distributed traces with `TracerProtocol`, run health checks via `HealthChecker`, and profile async functions. Backends for Prometheus and OpenTelemetry.

## Installation

```bash
pip install lexigram-monitor
```

## Quick Start

```python
from lexigram.monitor.module import MonitorModule
from lexigram.monitor.backends import PrometheusBackend

app.add_module(MonitorModule.configure(backend=PrometheusBackend()))
```

## Key Features

- Metrics: `Counter`, `Gauge`, `Histogram`, `Summary` with `MetricsRecorderProtocol`
- Tracing: `Tracer`, `Span`, `SpanExporter` with OTLP and console exporters
- Health checks: `HealthChecker`, `HealthCheckRegistry`, `FunctionHealthCheck`
- Profiling: `PerformanceMonitor` with snapshot and async profiling
- No-op stubs for testing (`NoOpTracer`, `NoOpMetricsCollector`)

## Configuration

Provide a `MetricsBackendProtocol` implementation. OpenTelemetry, Prometheus, and NoOp backends included.

## Related

- [Guide](/guides/monitoring/)
- [`lexigram-resilience`](/ecosystem/lexigram-resilience/) — circuit breakers, retries
