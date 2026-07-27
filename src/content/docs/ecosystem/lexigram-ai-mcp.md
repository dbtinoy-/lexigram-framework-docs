---
title: "lexigram-ai-mcp"
description: "Model Context Protocol (MCP) server and client — tools, resources, prompts, and transport over stdio/SSE."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

`lexigram-ai-mcp` provides both an MCP server (exposing tools, resources, and prompts via stdio or SSE transport) and an MCP client for connecting to external MCP servers. Supports controller-based tool registration and auto-exposure of service methods.

## Installation

```bash
pip install lexigram-ai-mcp
```

## Quick Start

```python
from lexigram.ai.mcp import MCPModule

module = MCPModule.configure(
    controllers=[MyToolController],
)
```

## Key Features

- MCP server with stdio and SSE transports
- `MCPController` subclasses for declarative tool/resource/prompt registration
- `MCPClientModule` for connecting to external MCP servers
- Service auto-exposure — expose existing service methods as MCP tools
- `@tool`, `@resource`, `@prompt` decorators for inline definition

## Configuration

`MCPModule.configure(controllers=[...])` registers controller classes. `MCPModule.from_services(services=[...])` auto-exposes service methods. `MCPClientModule.configure(connections=[...])` sets up client connections.

## Related

- [Guide](/guides/ai-mcp/)
- [Skills](/ecosystem/lexigram-ai-skills/)
- [Agents](/ecosystem/lexigram-ai-agents/)
