---
title: "lexigram-audit"
description: "Append-only, HMAC-verified audit trail with configurable retention."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Record every business event to an immutable audit log. Entries are HMAC-checksummed for tamper detection, retained per policy, and queryable via `AuditStoreProtocol`.

## Installation

```bash
pip install lexigram-audit
```

## Quick Start

```python
from lexigram.audit.module import AuditModule

app.add_module(AuditModule.configure(
    hmac_key=b"secret",
    retention_days=365,
))
```

## Key Features

- Append-only store (SQL or in-memory) via `AuditStoreProtocol`
- HMAC-SHA256 checksum per entry via `compute_audit_checksum`
- Tamper verification via `AuditVerifier`
- Policy-based retention and automated purge
- Admin panel contributor for audit browsing

## Configuration

`AuditModule.configure()` accepts `hmac_key`, `store_backend`, `retention_days`, and `enable_admin`.

## Related

- [Guide](/guides/audit-trail/)
- [`lexigram-auth`](/ecosystem/lexigram-auth/) — authentication and authorization
