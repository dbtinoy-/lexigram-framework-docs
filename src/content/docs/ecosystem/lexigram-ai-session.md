---
title: "lexigram-ai-session"
description: "Conversation session management with branching, checkpointing, multi-agent rooms, and state machines."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-session` manages AI conversation sessions with branching (fork/merge), checkpoint/restore, context pruning, and multi-agent group sessions with role isolation and turn management.

## Installation

```bash
pip install lexigram-ai-session
```

## Quick Start

```python
from lexigram.ai.session import SessionModule
from lexigram.ai.session.config import SessionConfig

module = SessionModule.configure(
    SessionConfig(backend="cache"),
    enable_cleanup_scheduler=True,
)
```

## Key Features

- Branching: append merge, selective merge, branch manager
- Checkpointing: save and restore session state with diff tracking
- Multi-agent group sessions with role isolation and turn managers
- Session state machine, analytics, and background cleanup scheduler

## Configuration

`SessionConfig` accepts `backend` (`in-memory`, `cache`, `database`), TTL, and cleanup intervals. Supports pluggable session stores.

## Related

- [Guide](/guides/ai-sessions/)
- [Memory](/ecosystem/lexigram-ai-memory/)
- [Agents](/ecosystem/lexigram-ai-agents/)
