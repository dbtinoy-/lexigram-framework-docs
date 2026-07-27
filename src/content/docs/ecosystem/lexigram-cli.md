---
title: "lexigram-cli"
description: "The `lexigram` command — project scaffolding, dev server, database migrations, and inspection."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

The `lexigram` CLI accelerates development with commands for scaffolding new projects, running the dev server, managing database migrations, and inspecting application state.

## Installation

```bash
pip install lexigram-cli
```

## Quick Start

```bash
lexigram new myapp
cd myapp
lexigram dev
```

## Key Commands

| Command | Description |
|---------|-------------|
| `lexigram new` | Scaffold a new project from templates |
| `lexigram dev` | Start the development server with hot reload |
| `lexigram run` | Start the production server |
| `lexigram db` | Database migrations and management |
| `lexigram inspect` | Inspect application state |
| `lexigram shell` | Interactive Python shell with app context |
| `lexigram config` | View and validate configuration |
| `lexigram gen` | Generate providers, modules, and other artifacts |

## Configuration

`CLIModule.configure()` accepts a `CLIConfig`. The CLI discovers `lexigram.yaml` in the project root.

## Related

- [Guide](/guides/cli/)
- [Installation](/getting-started/installation/)
