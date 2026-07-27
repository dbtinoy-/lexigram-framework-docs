---
title: "lexigram-webhook"
description: "Outbound webhook management with HMAC-signed delivery, retry logic, and dead-letter queue."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Manage webhook subscriptions, delivery, and verification. HMAC-signs every payload, retries on failure with exponential backoff, and routes undeliverable messages to a dead-letter queue.

## Installation

```bash
pip install lexigram-webhook
```

## Quick Start

```python
from lexigram.webhook.module import WebhookModule

app.add_module(WebhookModule.configure())
```

## Key Features

- Subscription CRUD via `WebhookSubscriptionService`
- HMAC-signed delivery with automatic retry and DLQ
- Delivery attempt tracking via `WebhookDeliveryServiceProtocol`
- Pluggable subscription stores (SQL, memory)
- Admin panel widgets for delivery monitoring

## Configuration

Optional `WebhookConfig` for store backend, retry policy, and HMAC settings. Defaults to in-memory store.

## Related

- [Guide](/guides/webhooks/)
- [`lexigram-queue`](/ecosystem/lexigram-queue/) — message bus integration
