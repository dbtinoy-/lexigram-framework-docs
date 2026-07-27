---
title: "lexigram-auth"
description: "Authentication and authorization — JWT, OAuth2, RBAC, password hashing, API keys, and web guards."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Full auth stack with `AuthenticationService`, `JWTTokenManager`, `AuthorizationService`, `PasswordHasher`, and guard decorators (`require_auth`, `require_roles`, `require_permissions`). OAuth2/OIDC via `GoogleOAuthService`.

## Installation

```bash
pip install lexigram-auth
```

## Quick Start

```python
from lexigram.auth.module import AuthModule
from lexigram.auth.config import AuthConfig

app.add_module(AuthModule.configure(AuthConfig(secret_key="...")))
```

## Key Features

- JWT access/refresh tokens via `JWTTokenManager`
- RBAC with `AuthorizationService` and `RoleDefinition`
- Password hashing with `PasswordHasher` and `PasswordPolicy`
- API key authentication via `APIKeyAuthenticator`
- OAuth2 (Google) via `GoogleOAuthService`
- Guard decorators: `require_auth`, `require_roles`, `require_permissions`

## Configuration

`AuthModule.configure()` accepts an `AuthConfig` with JWT, RBAC, and lockout settings.

## Related

- [Guide](/guides/auth/)
- [`lexigram-audit`](/ecosystem/lexigram-audit/) — audit trail for auth events
