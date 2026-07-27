---
title: "lexigram-web"
description: "Progressive web framework — controllers, routing, middleware, OpenAPI, CORS, CSRF, and rate limiting."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Build HTTP APIs with controller-based routing, middleware pipelines, OpenAPI documentation, CORS/CSRF protection, and rate limiting. Built on top of the core DI container for clean dependency injection.

## Installation

```bash
pip install lexigram-web
```

## Quick Start

```python
from lexigram.web import WebModule, Controller, get

class HealthController(Controller):
    @get("/health")
    async def health(self) -> dict:
        return {"status": "ok"}

app.add_module(WebModule.configure(controllers=[HealthController]))
```

## Key Features

- Decorator-based controller routing (`@get`, `@post`, etc.)
- Middleware pipeline with `DefaultMiddlewareStack`
- OpenAPI schema generation via route introspection
- CORS, CSRF, and input sanitization middleware
- Rate limiting with `RateLimitModule`
- WebSocket support and HTMX responses

## Configuration

`WebConfig` manages server host/port, CORS origins, CSRF settings, and middleware configuration. Loaded from `[web]` section of `application.yaml`.

## Related

- [Guide](/guides/web/)
- [`lexigram-graphql`](/ecosystem/lexigram-graphql/) — GraphQL endpoint integration
