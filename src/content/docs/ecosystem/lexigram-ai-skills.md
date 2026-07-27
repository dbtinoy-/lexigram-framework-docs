---
title: "lexigram-ai-skills"
description: "Skill/tool registry and executor with built-in tools, composition, caching, and permission control."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-skills` provides a registry-based skill execution platform. Define skills via classes or decorators, compose them into chains and pipelines, and control access through a permission checker.

## Installation

```bash
pip install lexigram-ai-skills
```

## Quick Start

```python
from lexigram.ai.skills import SkillsModule
from lexigram.ai.skills.config import SkillsConfig

module = SkillsModule.configure(SkillsConfig(enable_cache=True))
```

## Key Features

- Declarative skills via `AbstractSkill` base class or `@skill` decorator
- Composition: chains, parallel execution, pipelines, and routers
- Built-in skills: code execution, database query, file I/O, HTTP, web search, math, text processing
- Caching, timeout enforcement, and permission-based access control

## Configuration

`SkillsConfig` controls cache settings, default timeout, permission checker, and discovery sources.

## Related

- [Guide](/guides/ai-skills/)
- [Agents](/ecosystem/lexigram-ai-agents/)
- [MCP](/ecosystem/lexigram-ai-mcp/)
