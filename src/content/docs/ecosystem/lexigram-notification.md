---
title: "lexigram-notification"
description: "Email, SMS, and push notification delivery with multi-backend Named DI support."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Email delivery via SMTP or SendGrid, SMS via Twilio, and push notifications via APNs, FCM, or WebPush. Includes an in-app inbox and a mailable abstraction.

## Installation

```bash
pip install lexigram-notification
```

## Quick Start

```python
from lexigram.notification.config import MailerConfig, NotificationConfig
from lexigram.notification.mailer.module import MailerModule
from lexigram.notification.module import NotificationModule

app.add_module(MailerModule.configure(MailerConfig(backends=[...])))
app.add_module(NotificationModule.configure(NotificationConfig(backends=[...])))
```

## Key Features

- Email backends: SMTP, SendGrid with `MailerProtocol`
- Push backends: APNs, FCM, WebPush with `PushChannelProtocol`
- SMS via Twilio with `SMSChannelProtocol`
- In-app inbox with `InboxService` and `InboxStoreProtocol`
- Named DI for multiple mailer/push/SMS configurations

## Configuration

Provide `MailerConfig` for email, `NotificationConfig` for SMS and push. Each supports named backends and primary/secondary routing.

## Related

- [Guide](/guides/notifications/)
- [`lexigram-webhook`](/ecosystem/lexigram-webhook/) — outbound webhook delivery
