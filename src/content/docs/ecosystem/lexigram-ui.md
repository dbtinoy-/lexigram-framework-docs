---
title: "lexigram-ui"
description: "Server-rendered HTMX/htpy component library — atoms, molecules, organisms, and layouts."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Server-rendered UI primitives — components, layouts, HTMX helpers, and rendering utilities — built on htpy for plain Python templates. Ships with atoms (Button, TextInput, Badge), molecules (Card, Modal, Tabs), organisms (Form, SlideOver), and layouts, all integrated via `UIModule` for DI wiring and config-driven defaults.

## Installation

```bash
uv add lexigram-ui
```

## Quick Start

```python
from lexigram.ui.atoms import Button
from lexigram.ui.core.base import render_to_string

button = Button("Click me", variant="primary")
html = render_to_string(button)
```

## Key Features

- Atoms, molecules, organisms component hierarchy
- ShadCN-compatible CSS variable design tokens
- HTMX response helpers and middleware integration
- Theme system with customizable color schemes
- Component CLI (`lexigram-ui add`) for scaffolding
- Polymorphic `asChild` pattern for slot-based composition

## Configuration

`UIConfig` manages theme selection, SSE settings, and default component configuration. Loaded from `[ui]` section of `application.yaml`.

## Related

- [Guide](/guides/ui/)
- [`lexigram-web`](/ecosystem/lexigram-web/) — Web framework
