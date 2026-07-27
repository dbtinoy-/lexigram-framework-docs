---
title: "lexigram-ai-agents"
description: "Agent framework with tool registry, ReAct/plan-and-execute strategies, multi-agent crews, and delegation."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-agents` provides a composable agent system with pluggable reasoning strategies, a tool registry, multi-agent crews, and delegation via agent-as-tool adapters.

## Installation

```bash
pip install lexigram-ai-agents
```

## Quick Start

```python
from lexigram.ai.agents import AgentsModule, AgentConfig
from lexigram.ai.agents import AgentBase, tool

module = AgentsModule.configure(AgentConfig(max_iterations=10))
```

## Key Features

- Strategies: ReAct, Plan-and-Execute, Reflexion, Supervisor
- Tool registry with permission checking and caching
- Multi-agent crews with round-robin and priority turn management
- Agent-as-tool delegation for hierarchical agent topologies

## Configuration

`AgentConfig` controls `max_iterations`, `budget`, default strategy, and tool permissions. Use `AgentsModule.configure(enable_multi_agent=True)` to activate crew support.

## Related

- [Guide](/guides/ai-agents/)
- [Skills](/ecosystem/lexigram-ai-skills/)
- [Sessions](/ecosystem/lexigram-ai-session/)
