---
title: Lexigram-Auth API
description: Lexigram-Auth API guide and reference for the lexigram-auth package in the Lexigram framework.
---

## __init__.py
  # lexigram-auth — Authentication and authorisation for the Lexigram platform.

- def __getattr__(name: str) -> Any
    # Lazy load attributes to avoid circular imports.

- def __dir__() -> list[str]
    # List available attributes for IDE support.

## admin/contributor.py
  # Admin contributor for lexigram-auth — surfaces session, token, and login

+ class AuthAdminContributor:
    # Admin contributor for the lexigram-auth package.
    __init__(self) -> None
    + def __init__(self) -> None
        # Initialize the contributor with no arguments.
    + async def on_admin_boot(self, container: ContainerResolverProtocol) -> None
        # Resolve auth DI dependencies from the container.
    + def get_dashboard_widgets(self) -> Sequence[DashboardWidgetDefinition]
        # Return the dashboard widget definitions for this contributor.
    + def get_navigation_items(self) -> Sequence[NavigationContribution]
        # Return the navigation items for this contributor.
    + def get_health_definitions(self) -> Sequence[AdminHealthDefinition]
        # Return the health check definitions for this contributor.
    + def get_actions(self) -> Sequence[AdminActionDefinition]
        # Return the action definitions for this contributor.
    + async def render_widget(self, widget_name: str, params: WidgetParams) -> Result[WidgetViewModel, AdminError]
        # Render a widget HTML via registry dispatch.

## admin/handlers/active_sessions.py
  # Active sessions widget handler.

+ class ActiveSessionsWidgetHandler:
    # Handler for the active sessions widget.
    __init__(self, session_manager: SessionManagerProtocol) -> None
    + def __init__(self, session_manager: SessionManagerProtocol) -> None
        # Initialize handler with session manager.
    + async def get_data(self, params: WidgetParams) -> Result[ActiveSessionsViewModel, AdminError]
        # Fetch active sessions data.

## admin/handlers/failed_logins.py
  # Failed logins widget handler.

+ class FailedLoginsWidgetHandler:
    # Handler for the failed logins widget.
    __init__(self, session_manager: SessionManagerProtocol) -> None
    + def __init__(self, session_manager: SessionManagerProtocol) -> None
        # Initialize handler with session manager.
    + async def get_data(self, params: WidgetParams) -> Result[FailedLoginsViewModel, AdminError]
        # Fetch failed login statistics.

## admin/handlers/token_refresh_rate.py
  # Token refresh rate widget handler.

+ class TokenRefreshRateWidgetHandler:
    # Handler for the token refresh rate widget.
    __init__(self, session_manager: SessionManagerProtocol) -> None
    + def __init__(self, session_manager: SessionManagerProtocol) -> None
        # Initialize handler with session manager.
    + async def get_data(self, params: WidgetParams) -> Result[TokenRefreshRateViewModel, AdminError]
        # Fetch token refresh rate data.

## admin/renderer.py
  # Jinja2 widget renderer for auth admin widgets.

+ class PackageWidgetRenderer:
    # Renders admin widget templates for lexigram-auth.
    __init__(self) -> None
    + def __init__(self) -> None
        # Initialize renderer with the package templates directory.
    + def render(self, template_name: str, context: dict[str, Any]) -> str
        # Render a template with context.

## admin/viewmodels.py
  # Frozen viewmodels for auth admin widgets.

+ @dataclass(frozen=True)
+ class ActiveSessionsViewModel:
    # Data model for active sessions widget.

+ @dataclass(frozen=True)
+ class TokenRefreshRateViewModel:
    # Data model for token refresh rate widget.

+ @dataclass(frozen=True)
+ class FailedLoginsViewModel:
    # Data model for failed logins widget.

## authn/_binding.py
  # JWT token binding configuration and helpers.

+ @dataclass
+ class TokenBindingConfig:
    # Configuration for opt-in JWT client binding.
    bind_to_ip: bool = False
    bind_to_fingerprint: bool = False
    fingerprint_header: str = 'X-Client-Fingerprint'

+ def compute_binding_hash(config: TokenBindingConfig, ctx: dict[str, str]) -> str | None
    # Compute a binding hash from the provided context.

+ def verify_binding(config: TokenBindingConfig, claims: dict[str, object], ctx: dict[str, str]) -> bool
    # Verify that the token binding hash matches the current context.

## authn/_jwt_creation.py
  # Token creation mixin for :class:`~lexigram.auth.authn.jwt.JWTTokenManager`.

- class _JWTCreationMixin:
    # Mixin providing JWT token-creation methods for :class:`JWTTokenManager`.
    __init__(self, ids: IdGeneratorProtocol | None = None) -> None
    + def __init__(self, ids: IdGeneratorProtocol | None = None) -> None
        # Initialize the JWT creation mixin.
    + @property
    + def current_key_id(self) -> str
        # Active signing key ID — provided by JWTTokenManager.
    - def _get_signing_key(self) -> str
        # Return raw signing key — provided by JWTTokenManager.
    + def create_access_token(self, user: User, additional_claims: dict[str, Any] | None = None, binding_context: dict[str, str] | None = None) -> str
        # Create a JWT access token for a user with current key.
    + def create_refresh_token(self, user: User, binding_context: dict[str, str] | None = None) -> str
        # Create a JWT refresh token for a user.
    + def create_token_pair(self, user: User, additional_claims: dict[str, Any] | None = None, binding_context: dict[str, str] | None = None) -> AuthToken
        # Create both access and refresh tokens.
    + def create_token(self, user: Any, additional_claims: dict[str, Any] | None = None, binding_context: dict[str, str] | None = None) -> AuthToken
        # Create auth tokens for a user, satisfying the TokenManagerProtocol protocol.

## authn/_jwt_lifecycle.py
  # Token verification and lifecycle mixin for :class:`~lexigram.auth.authn.jwt.JWTTokenManager`.

- class _JWTLifecycleMixin:
    # Mixin providing JWT token verification and lifecycle methods for :class:`JWTTokenManager`.
    + @property
    + def keys(self) -> dict[str, Any]
        # Live key material — provided by JWTTokenManager.
    + @property
    + def current_key_id(self) -> str
        # Active signing key ID — provided by JWTTokenManager.
    - def _get_verification_key(self, kid: str) -> str
        # Return raw verification key — provided by JWTTokenManager.
    + def create_token_pair(self, user: User, additional_claims: dict[str, Any] | None = None, binding_context: dict[str, str] | None = None) -> AuthToken
        # Create token pair — provided by _JWTCreationMixin.
    - async def _emit_action(self, hook_name: str, payload: object) -> None
        # Emit a token lifecycle hook when a registry is available.
    + async def refresh_token(self, refresh_token: str) -> Result[AuthToken, ContractsTokenError]
        # Refresh an access token using a refresh token.
    + async def refresh_with_rotation(self, refresh_token: str) -> Result[TokenPair, ContractsTokenError]
        # Rotate a refresh token and return a new access + refresh token pair.
    + async def verify_token(self, token: str, token_type: str = 'access', expected_audience: str | None = None, required_scope: str | None = None, binding_context: dict[str, str] | None = None, allow_missing_audience: bool) -> Result[VerifiedToken, ContractsTokenError]
        # Verify and decode a JWT token with support for multiple keys.
    + async def logout(self, token: str) -> Result[None, ContractsTokenError]
        # Invalidate a token by adding it to the blacklist.
    + async def logout_all_user_tokens(self, user_id: str) -> Result[None, ContractsTokenError]
        # Invalidate all tokens for a user by writing a user-level blacklist entry.
    - async def _is_token_blacklisted(self, token: str) -> bool
        # Check if a token is blacklisted.
    + async def refresh_access_token(self, refresh_token: str) -> AuthToken
        # Create new access token from refresh token with rotation.
    + async def get_user_from_token(self, token: str) -> Result[VerifiedToken, ContractsTokenError]
        # Extract user information from access token.

## authn/_key_utils.py
  # JWT key normalization utilities.

+ def normalize_jwt_keys(keys: dict[str, Any]) -> dict[str, SecretStr | dict[str, SecretStr]]
    # Coerce all JWT key material to :class:`~lexigram.validation.SecretStr`.

## authn/account_verification.py
  # Account verification service for Lexigram Auth.

+ class AccountVerificationError:
    # Error during account verification operations.

+ @inject
+ class AccountVerificationService:
    # Service for handling account verification flows.
    __init__(self, user_store: UserStoreProtocol, token_ttl_days: int = TOKEN_EXPIRY_DAYS) -> None
    + def __init__(self, user_store: UserStoreProtocol, token_ttl_days: int = TOKEN_EXPIRY_DAYS) -> None
    + def generate_verification_token(self) -> tuple[str, datetime]
        # Generate a secure random verification token.
    + async def send_verification(self, user_id: str) -> Result[tuple[str, datetime], AlreadyVerifiedError | UserNotFoundError]
        # Send verification email for a user.
    + async def verify(self, token: str) -> Result[None, ContractsVerificationError]
        # Verify user account with token.
    - async def _find_user_by_token(self, token: str) -> Any | None
        # Find user by verification token.
    + async def resend_verification(self, email: str) -> Result[tuple[str, datetime], AlreadyVerifiedError | UserNotFoundError]
        # Resend verification token.
    + def __repr__(self) -> str

## authn/blacklist.py
  # JWT token blacklist management.

+ class JWTBlacklist:
    # Hash-based JWT blacklist supporting both cache and in-process storage.
    __init__(self, cache: CacheBackendProtocol | None, algorithm: str, current_key_id_fn: Any, access_expiration_hours: int, refresh_expiration_days: int, audit_logger: AuditLoggerProtocol | None = None) -> None
    + def __init__(self, cache: CacheBackendProtocol | None, algorithm: str, current_key_id_fn: Any, access_expiration_hours: int, refresh_expiration_days: int, audit_logger: AuditLoggerProtocol | None = None) -> None
    + async def revoke(self, token: str) -> Result[None, ContractsTokenError]
        # Add *token* to the blacklist.
    + async def revoke_all_for_user(self, user_id: str) -> Result[None, ContractsTokenError]
        # Blacklist all tokens for *user_id* by writing a user-level sentinel.
    + async def is_blacklisted(self, token: str) -> bool
        # Return ``True`` if *token* has been revoked.

## authn/google_oauth.py
  # Google OAuth verification and claim normalization helpers.

+ class GoogleOAuthService:
    # Verify Google OAuth tokens and normalize the verified claims.
    __init__(self, client_id: str, http_client: HTTPClientProtocol | None, jwks_url: str, tokeninfo_url: str, userinfo_url: str, allowed_issuers: tuple[str, ...], jwks_cache_ttl_seconds: int) -> None
    + def __init__(self, client_id: str, http_client: HTTPClientProtocol | None, jwks_url: str, tokeninfo_url: str, userinfo_url: str, allowed_issuers: tuple[str, ...], jwks_cache_ttl_seconds: int) -> None
    + async def verify_token(self, token: str) -> VerifiedIdentityClaims
        # Verify a Google token, preferring ID-token JWKS validation.
    + async def verify_id_token(self, token: str) -> VerifiedIdentityClaims
        # Verify a Google ID token against Google's JWKS.
    + async def verify_userinfo_token(self, token: str) -> VerifiedIdentityClaims
        # Verify a Google access token via the userinfo endpoint.
    + async def verify_tokeninfo(self, token: str) -> VerifiedIdentityClaims
        # Verify a Google token using the tokeninfo endpoint fallback.
    - async def _get_jwks(self) -> dict[str, Any]
        # Fetch Google's JWKS, caching it for a short TTL.
    - def _select_jwk(self, jwks: dict[str, Any], kid: str | None) -> dict[str, Any]
        # Select the matching JWK for a token header.
    - async def _request_json(self, method: str, url: str, **kwargs: Any) -> dict[str, Any]
        # Fetch JSON via the injected HTTP client or a temporary httpx client.
    - async def _response_json(self, response: HttpResponse | Any) -> dict[str, Any]
        # Normalise framework HTTP responses and test doubles to JSON dicts.
    - def _claims_from_payload(self, payload: dict[str, Any], issuer: str | None, audience: str | None) -> VerifiedIdentityClaims
        # Convert Google payloads into normalized verified identity claims.
    - def _timestamp_to_datetime(self, value: Any) -> datetime | None
        # Convert a numeric UNIX timestamp to UTC datetime.
    - @staticmethod
    - def _looks_like_jwt(token: str) -> bool
        # Return True when the token resembles a JWT.

+ global GOOGLE_ISSUERS: tuple[str, str]

+ global GOOGLE_JWKS_URL

+ global GOOGLE_TOKENINFO_URL

+ global GOOGLE_USERINFO_URL

## authn/jwt.py
  # JWT token management for authentication.

+ class JWTTokenManager:
    # JWT token management with key rotation support.
    __init__(self, current_key_id: str, keys: dict[str, str | SecretStr | dict[str, str | SecretStr]] | None = None, algorithm: str = const.DEFAULT_TOKEN_ALGORITHM, access_expiration_hours: int = 24, refresh_expiration_days: int = 30, cache_service: CacheBackendProtocol | None = None, rotation_interval_days: int = 90, grace_period_seconds: int = const.DEFAULT_JWT_KEY_ROTATION_GRACE_PERIOD_SECONDS, logger: Logger | None = None, audit_logger: AuditLoggerProtocol | None, binding_config: TokenBindingConfig | None, required_audience: str | None, ids: IdGeneratorProtocol | None, allow_unverified_dev: bool) -> None
    + def __init__(self, current_key_id: str, keys: dict[str, str | SecretStr | dict[str, str | SecretStr]] | None = None, algorithm: str = const.DEFAULT_TOKEN_ALGORITHM, access_expiration_hours: int = 24, refresh_expiration_days: int = 30, cache_service: CacheBackendProtocol | None = None, rotation_interval_days: int = 90, grace_period_seconds: int = const.DEFAULT_JWT_KEY_ROTATION_GRACE_PERIOD_SECONDS, logger: Logger | None = None, audit_logger: AuditLoggerProtocol | None, binding_config: TokenBindingConfig | None, required_audience: str | None, ids: IdGeneratorProtocol | None, allow_unverified_dev: bool) -> None
        # Initialize the JWT token manager.
    + @property
    + def keys(self) -> dict[str, Any]
        # Live view of the key material managed by the key store.
    - @property
    - def _key_meta(self) -> dict[str, Any]
        # Live view of the key metadata managed by the key store.
    + @property
    + def current_key_id(self) -> str
        # The key ID currently used for signing new tokens.
    + @setter
    + def current_key_id(self, value: str) -> None
        # Allow external callers to update the active key ID on the store.
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    + def set_hook_registry(self, hooks: HookRegistryProtocol | None) -> None
        # Attach an optional hook registry after provider boot wiring.
    + async def rotate_key(self, new_key_id: str, new_secret: str | dict) -> None
        # Rotate to a new signing key, delegating lifecycle to the key store.
    - async def _cleanup_old_keys(self) -> None
        # Delegate old-key cleanup to the key store.
    + def list_keys(self) -> dict[str, dict[str, Any]]
        # Return current key metadata (for inspection/operations).
    - def _get_signing_key(self) -> str
        # Return the raw signing key string for the current key ID.
    - def _get_verification_key(self, kid: str) -> str
        # Return the raw verification key string for *kid*.
    + async def get_user_from_token(self, token: str) -> Result[VerifiedToken, ContractsTokenError]
        # Extract user information from access token.

## authn/key_rotation.py
  # JWT key rotation helpers.

+ class JWTKeyStore:
    # Manages JWT signing keys with support for seamless rotation.
    __init__(self, current_key_id: str, keys: dict[str, Any] | None = None, grace_period_seconds: float = 3600.0) -> None
    + def __init__(self, current_key_id: str, keys: dict[str, Any] | None = None, grace_period_seconds: float = 3600.0) -> None
    + async def rotate(self, new_key_id: str, new_secret: str | dict) -> None
        # Switch to a new signing key, retaining the old one for the grace period.
    - async def _cleanup_old_keys(self) -> None
        # Remove keys that have been retired beyond the grace period.
    + def get_signing_key(self) -> str
        # Return the raw signing key string for the current key ID.
    + def get_verification_key(self, kid: str) -> str | None
        # Return the raw verification key string for *kid*, or ``None``.
    + def list_keys(self) -> dict[str, dict[str, Any]]
        # Return a copy of the key metadata dict (for inspection/auditing).

## authn/ldap.py
  # LDAP authentication manager implementation.

+ @dataclass
+ class LDAPProvider:
    # LDAP provider configuration.
    name: str
    server_url: str
    bind_dn: str | None = None
    bind_password: SecretStr | None = None
    user_search_base: str = ''
    user_search_filter: str = '(sAMAccountName={username})'
    user_dn_attribute: str = 'distinguishedName'
    group_search_base: str | None = None
    group_search_filter: str | None = None
    require_group_membership: str | None = None
    tls_ca_cert_file: str | None = None
    tls_cert_file: str | None = None
    tls_key_file: str | None = None
    timeout: int = 30
    max_connections: int = 10

+ class LDAPManager:
    # Manager for LDAP/Active Directory authentication operations.
    __init__(self, providers: dict[str, Any], http_client: HTTPClientProtocol | None = None) -> None
    + def __init__(self, providers: dict[str, Any], http_client: HTTPClientProtocol | None = None) -> 
        # Initialize LDAP manager.
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    + async def authenticate_user(self, provider_name: str, username: str, password: str) -> dict[str, Any] | None
        # Authenticate a user against LDAP.
    + async def get_user_info(self, provider_name: str, username: str) -> dict[str, Any] | None
        # Get user information from LDAP without authentication.
    + async def check_group_membership(self, provider_name: str, username: str, group_name: str) -> bool
        # Check if user is a member of the specified group.
    - async def _get_user_dn(self, provider: LDAPProvider, username: str) -> str | None
        # Get the DN for a username by searching LDAP.
    - async def _get_group_dn(self, provider: LDAPProvider, group_name: str) -> str | None
        # Get the DN for a group by searching LDAP.
    - async def _bind_with_credentials(self, provider: LDAPProvider, user_dn: str, password: str) -> bool
        # Attempt to bind to LDAP with user credentials.
    - async def _get_user_attributes(self, provider: LDAPProvider, user_dn: str) -> dict[str, Any]
        # Get user attributes from LDAP.
    - async def _get_connection(self, provider: LDAPProvider) -> Connection
        # Get a connection from the pool or create a new one.
    - def _return_connection(self, provider: LDAPProvider, conn: Connection) -> None
        # Return a connection to the pool.

## authn/mfa.py
  # MFA utilities - TOTP (RFC 6238) and backup codes

- def _int_to_bytes(i: int) -> bytes

+ def generate_totp_secret(length: int = 20) -> str
    # Generate a base32-encoded secret for TOTP.

- def _hotp(secret: str, counter: int, digits: int = DEFAULT_TOTP_DIGITS) -> str

- def _normalize_base32(secret: str) -> str
    # Normalize base32 secret by adding padding if necessary

+ def generate_totp_code(secret: str, for_time: int | None = None, period: int = DEFAULT_TOTP_PERIOD, digits: int = DEFAULT_TOTP_DIGITS) -> str
    # Generate TOTP code for given secret and time (unix seconds).

+ def verify_totp(secret: str, code: str, window: int = 1, period: int = DEFAULT_TOTP_PERIOD) -> bool
    # Verify a TOTP code allowing a +/- window of time steps.

+ def get_provisioning_uri(secret: str, username: str, issuer: str) -> str
    # Return an `otpauth://` provisioning URI suitable for authenticator apps.

+ def generate_backup_codes(count: int = 10, length: int = 8) -> list[str]
    # Generate a list of human-friendly backup codes (plain strings).

+ def hash_backup_codes(codes: Iterable[str]) -> list[str]
    # Return digest hashes for backup codes (store these, compare with digest).

+ global DEFAULT_TOTP_DIGITS

+ global DEFAULT_TOTP_ALGORITHM

+ global DEFAULT_TOTP_PERIOD

## authn/oauth2.py
  # OAuth2 authentication flows.

+ class LexigramConnectSession:
    # Session adapter for authlib that delegates to ``HTTPClientProtocol``.
    __init__(self, http_client: HTTPClientProtocol | None) -> None
    + def __init__(self, http_client: HTTPClientProtocol | None) -> 
    + async def request(self, method: str, url: str, **kwargs: Any) -> LexigramConnectResponse
        # Make a request using the injected ``HTTPClientProtocol``.
    + async def get(self, url: str, **kwargs: Any) -> LexigramConnectResponse
    + async def post(self, url: str, **kwargs: Any) -> LexigramConnectResponse
    + async def put(self, url: str, **kwargs: Any) -> LexigramConnectResponse
    + async def delete(self, url: str, **kwargs: Any) -> LexigramConnectResponse
    + async def patch(self, url: str, **kwargs: Any) -> LexigramConnectResponse
    + async def head(self, url: str, **kwargs: Any) -> LexigramConnectResponse

+ class LexigramConnectResponse:
    # Response adapter that makes any HTTP response compatible with authlib.
    __init__(self, response: Any) -> None
    + def __init__(self, response: Any) -> 
    + @property
    + def status_code(self) -> int
    + @property
    + def headers(self) -> dict[str, str]
    + async def json(self) -> dict[str, Any]
    + async def text(self) -> str
    + def raise_for_status(self) -> None
    + async def close(self) -> None
        # Close the underlying response if the client supports it.
    + async def __aenter__(self) -> Self
    + async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: object) -> None

+ class OAuth2IdentityProvider:
    # OAuth2 identity provider configuration.
    __init__(self, name: str, client_id: str, client_secret: str, authorize_url: str, access_token_url: str, userinfo_url: str, scope: str = 'openid email profile', redirect_uri: str | None = None, require_pkce: bool = True) -> None
    + def __init__(self, name: str, client_id: str, client_secret: str, authorize_url: str, access_token_url: str, userinfo_url: str, scope: str = 'openid email profile', redirect_uri: str | None = None, require_pkce: bool = True) -> 

+ class OAuth2Manager:
    # OAuth2 authentication manager
    __init__(self, providers: dict[str, OAuth2IdentityProvider], http_client: HTTPClientProtocol | None = None) -> None
    + def __init__(self, providers: dict[str, OAuth2IdentityProvider], http_client: HTTPClientProtocol | None = None) -> None
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    + async def get_authorization_url(self, provider_name: str, state: str | None = None) -> tuple[str, str, str]
        # Get OAuth2 authorization URL, PKCE code_verifier (S256), and state.
    + async def exchange_code_for_token(self, provider_name: str, code: str, code_verifier: str | None = None) -> dict[str, Any]
        # Exchange authorization code for access token, optionally with PKCE code_verifier
    + async def get_user_info(self, provider_name: str, token: dict[str, Any]) -> dict[str, Any]
        # Get user information from OAuth2 provider

+ class OAuth2AuthProvider:
    # Complete OAuth2 provider with user provisioning.
    __init__(self, oauth2_manager: OAuth2Manager, user_store: Any, oauth_identity_store: Any | None = None) -> None
    + def __init__(self, oauth2_manager: OAuth2Manager, user_store: Any, oauth_identity_store: Any | None = None) -> None
    + async def authenticate_with_oauth2(self, provider_name: str, code: str, code_verifier: str | None = None) -> User
        # Authenticate user via OAuth2 and provision if needed.
    - async def _find_or_create_oauth_user(self, oauth_user: OAuth2UserInfo) -> User
        # Find existing user or provision new one.
    - async def _find_by_oauth_identity(self, provider: str, provider_user_id: str) -> User | None
        # Find user by OAuth identity.
    - async def _link_oauth_identity(self, user_id: str, provider: str, provider_user_id: str) -> None
        # Link OAuth identity to user.

## authn/passkeys.py
  # Minimal WebAuthn / Passkeys helper (server-side operations)

- class _PendingStore:
    # Abstract pending store with optional async cache backend.
    __init__(self, cache: CacheBackendProtocol | None = None) -> None
    + def __init__(self, cache: CacheBackendProtocol | None = None) -> None
    + async def set(self, key: str, value: dict, ttl: int = 300) -> None
    + async def get(self, key: str) -> dict | None
    + async def delete(self, key: str) -> None

+ @inject
+ class PasskeyService:
    # Manage passkey registration and authentication flows.
    __init__(self, user_store: UserStoreProtocol, cache_service: CacheBackendProtocol | None = None, rp_id: str | None, allowed_origins: set[str] | None) -> None
    + def __init__(self, user_store: UserStoreProtocol, cache_service: CacheBackendProtocol | None = None, rp_id: str | None, allowed_origins: set[str] | None) -> None
    - def _gen_challenge(self) -> str
    - def _validate_origin(self, origin: str | None) -> bool
        # Return False if origin is required but invalid or missing.
    + async def start_registration(self, user_id: str, name: str | None = None) -> tuple[str, str]
        # Start registration: return (registration_id, challenge).
    + async def finish_registration(self, registration_id: str, credential_id: str, public_key_pem: str, actor_user_id: str | None = None, origin: str | None) -> bool
        # Finish registration by storing the passkey on the user's profile.
    + async def start_authentication(self, user_id: str) -> tuple[str, str, list[str]]
        # Start authn: return (auth_id, challenge, allowed_credential_ids).
    + async def finish_authentication(self, auth_id: str, credential_id: str, signature: bytes, origin: str | None, new_sign_count: int | None) -> bool
        # Finish authentication by verifying the signature over the challenge.

## authn/password_hasher.py
  # Argon2id-based password hashing implementations.

+ class Argon2idKeyDerivation:
    # Argon2id key derivation implementation.
    __init__(self, config: PasswordConfig | None = None) -> None
    + def __init__(self, config: PasswordConfig | None = None) -> None
    + async def derive(self, secret: str, salt: bytes | None) -> str
        # Derive a key from a secret using Argon2id.
    + async def verify(self, secret: str, encoded: str) -> bool
        # Verify a secret against an Argon2id hash.
    + async def hash(self, secret: str, salt: bytes | None) -> str
        # Backward-compatible alias for derive.

+ class Argon2idPasswordHasher:
    # Auth-domain password hasher using Argon2id.
    __init__(self, kdf: KeyDerivationProtocol) -> None
    + def __init__(self, kdf: KeyDerivationProtocol) -> None
    + async def hash(self, password: str) -> str
        # Hash a password using Argon2id.
    + async def verify(self, password: str, hashed_password: str) -> bool
        # Verify a password against its hash.

## authn/password_reset.py
  # Password reset service for Lexigram Auth.

+ class PasswordResetTokenError:
    # Error during password reset token operations.

+ @inject
+ class PasswordResetService:
    # Service for handling password reset flows.
    __init__(self, user_store: UserStoreProtocol, token_ttl_hours: int = TOKEN_EXPIRY_HOURS) -> None
    + def __init__(self, user_store: UserStoreProtocol, token_ttl_hours: int = TOKEN_EXPIRY_HOURS) -> None
    + def generate_reset_token(self) -> tuple[str, datetime]
        # Generate a secure random reset token.
    + async def request_reset(self, email: str) -> Result[tuple[str, datetime] | None, PasswordResetTokenError]
        # Request a password reset for a user email.
    + async def confirm_reset(self, token: str, new_password: str) -> Result[None, PasswordResetTokenError]
        # Confirm password reset with new password.
    - async def _find_user_by_token(self, token: str) -> Any | None
        # Find user by reset token.
    + async def invalidate_token(self, user_id: str) -> None
        # Invalidate any pending reset token for a user.
    + def __repr__(self) -> str

## authn/revocation.py
  # Persistent token revocation store backed by a CacheBackendProtocol.

+ class PersistentTokenRevocationStore:
    # Persistent token revocation list backed by a :class:`CacheBackendProtocol`.
    __init__(self, cache: CacheBackendProtocol, ttl: int = _DEFAULT_TTL) -> None
    + def __init__(self, cache: CacheBackendProtocol, ttl: int = _DEFAULT_TTL) -> None
    - def _make_key(self, token_id: str) -> str
        # Return the cache key for a token ID.
    + async def revoke(self, token_id: str, expires_at: datetime | None = None) -> None
        # Mark *token_id* as revoked.
    + async def is_revoked(self, token_id: str) -> bool
        # Return ``True`` if *token_id* is present in the revocation list.

## authn/saml.py
  # SAML 2.0 authentication flows

+ class SAMLAttributeMapper:
    # Protocol for SAML attribute mappers.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None ...

+ class EmailAttributeMapper:
    # Maps SAML email attribute to user info.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None

+ class NameAttributeMapper:
    # Maps SAML name attributes to user info.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None

+ class FirstNameAttributeMapper:
    # Maps SAML firstName/givenName attribute to user info.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None

+ class LastNameAttributeMapper:
    # Maps SAML lastName/surname attribute to user info.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None

+ class GroupsAttributeMapper:
    # Maps SAML groups attribute to user info.
    + def map_attribute(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None

+ class SAMLAttributeMapperRegistry:
    # Registry for SAML attribute mappers.
    __init__(self) -> None
    + def __init__(self) -> None
    + @classmethod
    + def with_defaults(cls) -> SAMLAttributeMapperRegistry
        # Create a registry pre-loaded with the standard attribute mappers.
    - def _register_default_mappers(self) -> None
        # Register the default attribute mappers.
    + def register_mapper(self, mapper: SAMLAttributeMapper) -> None
        # Register a custom attribute mapper.
    + def clear_mappers(self) -> None
        # Clear all registered mappers.
    + def get_mappers(self) -> list[SAMLAttributeMapper]
        # Get all registered mappers.
    + def map_attributes(self, ava: dict[str, list[str]], user_info: dict[str, Any]) -> None
        # Map all SAML attributes using registered mappers.

+ class SAMLProvider:
    # SAML identity provider configuration
    __init__(self, name: str, entity_id: str, sso_url: str, slo_url: str | None = None, x509_cert: str | None = None, name_id_format: str = NAMEID_FORMAT_EMAILADDRESS, want_assertions_signed: bool = True, want_response_signed: bool = True, want_logout_response_signed: bool = False, want_logout_request_signed: bool = False) -> None
    + def __init__(self, name: str, entity_id: str, sso_url: str, slo_url: str | None = None, x509_cert: str | None = None, name_id_format: str = NAMEID_FORMAT_EMAILADDRESS, want_assertions_signed: bool = True, want_response_signed: bool = True, want_logout_response_signed: bool = False, want_logout_request_signed: bool = False) -> 

+ class SAMLManager:
    # SAML 2.0 authentication manager
    __init__(self, providers: dict[str, SAMLProvider], http_client: Any | None = None) -> None
    + def __init__(self, providers: dict[str, SAMLProvider], http_client: Any | None = None) -> None
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    - def _create_saml_client(self, provider: SAMLProvider) -> Saml2Client
        # Create SAML client for a provider
    + async def get_login_url(self, provider_name: str, relay_state: str | None = None) -> str
        # Get SAML login URL for the given provider
    + async def process_assertion(self, provider_name: str, saml_response: str, relay_state: str | None = None) -> dict[str, Any]
        # Process SAML assertion response
    + async def get_logout_url(self, provider_name: str, name_id: str, session_index: str | None = None) -> str | None
        # Get SAML logout URL for the given provider
    + async def process_logout_response(self, provider_name: str, saml_response: str) -> bool
        # Process SAML logout response

## authn/schemas/requests.py

+ @dataclass(init=False)
+ class LoginRequest:
    email: str = Field(...)
    password: str = Field(...)
    remember_me: bool = Field(...)

+ @dataclass(init=False)
+ class RegisterRequest:
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    confirm_password: str = Field(...)
    profile: dict = Field(default_factory=...)

+ @dataclass(init=False)
+ class RefreshTokenRequest:
    refresh_token: str = Field(...)

+ @dataclass(init=False)
+ class PasswordResetRequest:
    email: str = Field(...)

+ @dataclass(init=False)
+ class PasswordResetConfirm:
    token: str = Field(...)
    new_password: str = Field(...)
    confirm_password: str = Field(...)

+ @dataclass(init=False)
+ class OAuth2AuthorizeRequest:
    response_type: str = Field(...)
    client_id: str = Field(...)
    redirect_uri: str | None = Field(...)
    scope: str = Field(...)
    state: str | None = Field(...)

+ @dataclass(init=False)
+ class OAuth2TokenRequest:
    grant_type: str = Field(...)
    code: str | None = Field(...)
    redirect_uri: str | None = Field(...)
    client_id: str | None = Field(...)
    client_secret: str | None = Field(...)
    refresh_token: str | None = Field(...)

## authn/schemas/responses.py

+ @dataclass(init=False)
+ class TokenResponse:
    access_token: str = Field(...)
    token_type: str = Field(...)
    expires_in: int = Field(...)
    refresh_token: str | None = Field(...)
    user: dict = Field(...)

## authn/schemas/user.py

+ @dataclass(init=False)
+ class UserProfile:
    user_id: str
    name: str
    email: str
    created_at: datetime
    is_active: bool = True
    is_verified: bool = False
    updated_at: datetime | None = None
    last_login_at: datetime | None = None
    login_count: int = 0
    roles: list[str] = Field(default_factory=...)
    permissions: list[str] = Field(default_factory=...)
    profile: dict = Field(default_factory=...)

## authn/security.py
  # Password security utilities using Passlib with a lightweight fallback.

+ class PasswordHasher:
    # Bcrypt password hasher implementing the PasswordHasherProtocol.
    __init__(self, rounds: int = _DEFAULT_BCRYPT_ROUNDS) -> None
    + def __init__(self, rounds: int = _DEFAULT_BCRYPT_ROUNDS) -> None
    + @staticmethod
    + async def hash(password: str) -> str
        # Hash a password using bcrypt with UTF-8 aware truncation.
    + @staticmethod
    + async def verify(password: str, hashed_password: str) -> bool
        # Verify a password against its hash asynchronously.
    + def needs_rehash(self, hashed_password: str) -> bool
        # Check if the hash needs to be rehashed.
    + async def rehash_if_needed(self, password: str, hashed_password: str | None) -> str | None
        # Rehash the password if needed.

+ class PasswordPolicy:
    # Password policy configuration.
    __init__(self, min_length: int = 8, max_length: int = 128, require_uppercase: bool = True, require_lowercase: bool = True, require_digits: bool = False, require_special: bool = False, prevent_common: bool = True, prevent_reuse: bool = False, history_size: int = 5, common_passwords_file: str | None = None, banned_patterns: list[str] | None = None) -> None
    + def __init__(self, min_length: int = 8, max_length: int = 128, require_uppercase: bool = True, require_lowercase: bool = True, require_digits: bool = False, require_special: bool = False, prevent_common: bool = True, prevent_reuse: bool = False, history_size: int = 5, common_passwords_file: str | None = None, banned_patterns: list[str] | None = None) -> 
    + @classmethod
    + def from_config(cls, config: PasswordConfig) -> PasswordPolicy
        # Build a ``PasswordPolicy`` from a ``PasswordConfig`` dataclass.
    - def _load_common_passwords(self, file_path: str | None) -> set[str]
        # Load common passwords from file (lazy-loaded).
    - def _get_common_passwords(self) -> set[str]
        # Return common passwords set, loading lazily on first access.
    + def validate(self, password: str) -> None
        # Validate password against policy.
    + def is_valid(self, password: str) -> bool
        # Return True if the password satisfies the policy without raising.

- def _prehash(password: str) -> str
    # Pre-hash *password* with SHA-256 to avoid bcrypt's 72-byte truncation.

- def _prepare_password_bytes(password: str) -> bytes
    # Return the bytes that bcrypt should hash for *password*.

+ global DUMMY_PASSWORD_HASH

## authn/services.py
  # Authentication services for user login, registration, and token management.

+ @dataclass
+ class LockoutConfig:
    # Configuration for account lockout on repeated failed login attempts.
    max_failed_attempts: int = 5
    lockout_duration_seconds: int = 300
    max_attempts: int

+ class LoginAttemptTracker:
    # Tracks failed login attempts and enforces account lockout.
    __init__(self, max_attempts: int = 5, lockout_duration_seconds: int = 900, cache: CacheBackendProtocol | None = None) -> None
    + def __init__(self, max_attempts: int = 5, lockout_duration_seconds: int = 900, cache: CacheBackendProtocol | None = None) -> None
    + async def is_locked(self, identifier: str) -> bool
        # Return ``True`` if *identifier* has exceeded the failure threshold.
    + async def record_failure(self, identifier: str) -> None
        # Record a failed authentication attempt for *identifier*.
    + async def clear(self, identifier: str) -> None
        # Remove all recorded failures for *identifier* (call on success).
    - async def _is_locked_cache(self, identifier: str) -> bool
    - async def _record_failure_cache(self, identifier: str) -> None
    - def _is_locked_local(self, identifier: str) -> bool
    - def _record_failure_local(self, identifier: str) -> None

+ @inject
+ class AuthenticationService:
    # Service for core authentication operations.
    __init__(self, password_policy: PasswordPolicy, user_store: UserStoreProtocol, token_manager: JWTTokenManager, lockout_config: LockoutConfig | None = None, event_bus: EventBusProtocol | None = None, tracker: LoginAttemptTracker | None = None, hooks: HookRegistryProtocol | None = None) -> None
    + def __init__(self, password_policy: PasswordPolicy, user_store: UserStoreProtocol, token_manager: JWTTokenManager, lockout_config: LockoutConfig | None = None, event_bus: EventBusProtocol | None = None, tracker: LoginAttemptTracker | None = None, hooks: HookRegistryProtocol | None = None) -> None
    + def __repr__(self) -> str
        # Return a string representation of this service.
    - def _emit(self, event: object) -> None
        # Fire-and-forget event publication.
    + def set_hook_registry(self, hooks: HookRegistryProtocol | None) -> None
        # Attach an optional hook registry after provider boot wiring.
    - async def _emit_action(self, hook_name: str, payload: object) -> None
        # Emit an auth action hook when a registry is available.
    + async def authenticate_user(self, email: str, password: str) -> Result[User, InvalidCredentialsError | AccountLockedError]
        # Authenticate a user with email and password.
    - async def _rehash_password_if_needed(self, user: User, password: str, creds: UserCredentials | None) -> None
        # Rehash password in background if needed.
    + async def register_user(self, request: RegisterRequest) -> Result[User, EmailExistsError | PasswordPolicyError]
        # Register a new user.
    + def create_token(self, user: User) -> AuthToken
        # Create an authentication token for a user.
    + async def verify_token(self, token: str) -> Result[VerifiedToken, TokenError]
        # Verify and decode an authentication token.
    + async def refresh_token(self, refresh_token: str) -> Result[AuthToken, TokenError]
        # Refresh an access token using a refresh token.
    + async def get_user_from_token(self, token: str) -> Result[VerifiedToken, TokenError]
        # Get user information from token.
    + async def shutdown(self) -> None
        # Cancel and await all pending background event tasks.

## authn/user_service.py
  # User management services for CRUD operations.

+ @inject
+ class UserService:
    # Service for user management operations.
    __init__(self, password_policy: PasswordPolicy, user_store: Any, event_bus: EventBusProtocol | None = None) -> None
    + def __init__(self, password_policy: PasswordPolicy, user_store: Any, event_bus: EventBusProtocol | None = None) -> None
    - def _emit(self, event: object) -> None
        # Fire-and-forget event publication.
    + async def create_user(self, name: str, email: str, password: str, roles: list[str] | None = None) -> Result[User, EmailExistsError | PasswordPolicyError]
        # Create a new user.
    + async def get_user(self, user_id: str) -> User | None
        # Get user by ID.
    + async def update_user(self, user: User) -> Result[User, UserNotFoundError | ValidationError]
        # Update user information.
    + async def delete_user(self, user_id: str) -> Result[None, UserNotFoundError]
        # Delete a user.
    + async def lock_user(self, user_id: str) -> Result[None, UserNotFoundError]
        # Deactivate (lock) a user account.
    + async def unlock_user(self, user_id: str) -> Result[None, UserNotFoundError]
        # Reactivate (unlock) a previously locked user account.
    + async def change_user_password(self, user_id: str, current_password: str, new_password: str) -> Result[None, InvalidCredentialsError | PasswordPolicyError]
        # Change a user's password (requires current password).
    + async def set_user_password(self, user_id: str, new_password: str, force: bool = False) -> None
        # Set a user's password (admin operation).
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # List users with pagination.
    + async def count_users(self) -> int
        # Count total users.
    + def __repr__(self) -> str
        # Return a string representation of this service.
    + async def shutdown(self) -> None
        # Cancel and await all pending background event tasks.

## authz/__init__.py
  # Authorization (AuthZ) - Permissions and access control

- def __getattr__(name: str) -> Any

- def __dir__() -> list[str]

## authz/_check_mixin.py
  # Authorization check mixin for AuthorizationService.

- class _AuthCheckMixin:
    # Mixin providing authorization check methods for AuthorizationService.
    - def _parse_list(self, val: Any) -> list[str]
        # Parse a value into a list of strings using the registry.
    + async def check_access(self, user: Any, allowed_roles: set[str], resource: str | None = None, action: str | None = None) -> bool
        # Core access check combining roles, inheritance, and permission patterns.
    + def has_any_role(self, user: Any, roles: list[str]) -> bool
        # Check if user has any of the given roles.
    + def has_any_permission(self, user: Any, permissions: list[str]) -> bool
        # Return True if user has at least one of the given permissions.
    + async def can(self, user: Any, action: str, resource: str) -> bool
        # Convenience alias: return True if user can perform action on resource.
    + async def authorize(self, user: Any, action: str, resource: Any) -> Result[bool, AuthorizationError]
        # Check whether *user* is allowed to perform *action* on *resource*.
    - def _get_effective_roles(self, user_roles: set[str]) -> set[str]
        # Resolve all roles including inherited ones.
    - def _get_user_permissions(self, effective_roles: set[str]) -> set[str]
        # Flatten all permissions from effective roles.
    - def _has_permission(self, user_permissions: set[str], required: str) -> bool
        # Check if required permission matches any user permission patterns.
    - def _flatten_roles(self, role_names: set[str]) -> set[str]
        # Recursively collect all parent roles for the given set of role names.

## authz/_parsers.py
  # Value parser classes for authorization service.

+ class ValueParser:
    # Protocol for value parsers.
    + def can_parse(self, val: Any) -> bool ...
    + def parse(self, val: Any) -> list[str] ...

+ class StringValueParser:
    # Parser for string values, including JSON-encoded lists.
    + def can_parse(self, val: Any) -> bool
    + def parse(self, val: Any) -> list[str]

+ class ListValueParser:
    # Parser for list values.
    + def can_parse(self, val: Any) -> bool
    + def parse(self, val: Any) -> list[str]

+ class NoneValueParser:
    # Parser for None values.
    + def can_parse(self, val: Any) -> bool
    + def parse(self, val: Any) -> list[str]

+ class ValueParserRegistry:
    # Registry for value parsers.
    __init__(self) -> None
    + def __init__(self) -> None
    - def _register_default_parsers(self) -> None
        # Register the default value parsers.
    + def register_parser(self, parser: ValueParser) -> None
        # Register a custom value parser.
    + def parse(self, val: Any) -> list[str]
        # Parse the value using registered parsers.

## authz/guards.py
  # Authorization guards and route protection decorators.

+ class AuthorizationGuard:
    # GuardProtocol that checks user roles and/or permissions.
    __init__(self, roles: list[str] | None = None, permissions: list[str] | None = None, auth_service: AuthorizationService | None = None) -> None
    + def __init__(self, roles: list[str] | None = None, permissions: list[str] | None = None, auth_service: AuthorizationService | None = None) -> None
    + async def check_authorization(self, user: User | None) -> bool
        # Return ``True`` if *user* satisfies all role and permission requirements.
    + def get_error_message(self) -> str
        # Build a human-readable description of the requirements.

+ class RouteGuard:
    # Wraps an :class:`AuthorizationGuard` and provides HTTP response helpers.
    __init__(self, guard: AuthorizationGuard) -> None
    + def __init__(self, guard: AuthorizationGuard) -> None
    + async def check_access(self, user: User | None) -> bool
        # Delegate to the underlying guard's ``check_authorization``.
    + async def get_deny_response(self) -> JSONResponse
        # Build a 403 JSON response describing what was required.

- def _find_request(args: tuple, kwargs: dict) -> Any
    # Extract the first Starlette-like request from positional or keyword args.

+ def require_auth(roles: list[str] | None = None, permissions: list[str] | None = None, optional: bool = False) -> Callable[, Callable]
    # Decorator that protects a route handler with authentication and RBAC/ABAC checks.

+ def require_roles(*roles: str) -> Callable[, Callable]
    # Shorthand decorator requiring the user to have at least one of *roles*.

+ def require_permissions(*permissions: str) -> Callable[, Callable]
    # Shorthand decorator requiring the user to hold all of *permissions*.

+ def optional_auth(func: Callable) -> Callable
    # Decorator that attaches optional auth: user is populated if present, never blocked.

## authz/scopes.py
  # OAuth2 scopes and scope management

+ class OAuthScope:
    # Standard OAuth2 scopes
    OPENID = 'openid'
    EMAIL = 'email'
    PROFILE = 'profile'
    ADDRESS = 'address'
    PHONE = 'phone'
    READ = 'read'
    WRITE = 'write'
    DELETE = 'delete'
    ADMIN = 'admin'

+ class ScopeManager:
    # Manages OAuth2 scopes and their mappings.
    __init__(self) -> None
    + def __init__(self) -> None
    + def get_scope_permissions(self, scope: str) -> set[str]
        # Get permissions associated with a scope.
    + def get_scopes_for_permissions(self, permissions: list[str]) -> set[str]
        # Get minimum scopes required for permissions.
    + def validate_scopes(self, requested_scopes: list[str], allowed_scopes: list[str]) -> list[str]
        # Validate requested scopes against allowed scopes.
    + def expand_scope_permissions(self, scopes: list[str]) -> set[str]
        # Expand scopes to their associated permissions.

## authz/service.py
  # Unified Authorization Service for Lexigram.

+ @runtime_checkable
+ class UserProtocol:

+ class AuthorizationService:
    # Central service for all authorization checks.
    __init__(self, permission_cache_ttl: float = 300.0, max_cache_entries: int, audit_logger: AuditLoggerProtocol | None) -> None
    + def __init__(self, permission_cache_ttl: float = 300.0, max_cache_entries: int, audit_logger: AuditLoggerProtocol | None) -> None
        # Initialize a new authorization service instance.
    + def set_policies(self, policies: list[Any]) -> None
        # Set the ABAC policies and initialize the engine.
    + def set_roles(self, roles: dict[str, RoleDefinition | dict[str, Any]]) -> None
        # Set the global role definitions (usually from config/seed).
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    + def register_role(self, name: str, role: RoleDefinition | dict[str, Any]) -> None
        # Register a role definition.
    + def get_role(self, name: str) -> Any | None
    + async def sync_from_db(self, container: Any) -> None
        # Load roles from database and merge with existing (YAML) roles.
    + def create_role(self, name: str, permissions: list[str] | None = None, inherits: list[str] | None = None) -> None
        # Create or update a role definition.
    + def add_role_permission(self, role_name: str, permission: str) -> None
        # Add a permission to an existing role.
    + def get_role_permissions(self, role: str) -> set[str]
        # Get all permissions for a role, including inherited ones.
    + def invalidate_user(self, user_id: str) -> None
        # Invalidate the permission cache for a specific user.

- def __getattr__(name: str) -> Any

## cli/checks.py
  # CLI health checks for lexigram-auth.

+ async def check_auth_service(container: ContainerResolverProtocol) -> dict[str, object]
    # Verify auth service and JWT manager are operational.

## cli/commands.py
  # Auth CLI command group factory.

+ def create_auth_app() -> typer.Typer
    # Create the `lexigram auth` command group.

## cli/contributor.py
  # Auth CLI contributor definitions.

+ class AuthCliContributor:
    # CLI contributor for the lexigram-auth package.
    + @property
    + def contributor_id(self) -> str
        # Return the contributor identifier.
    + def get_generators(self) -> list[GeneratorDefinition]
        # Return generator definitions for auth.
    + def get_commands(self) -> list[CommandContribution]
        # Return the contributed `auth` command group.
    + def get_health_checks(self) -> list[HealthCheckContribution]
        # Return auth service health check.
    + def get_doctor_checks(self) -> list[DoctorCheckContribution]
        # Return auth configuration doctor checks.
    + def get_shell_context(self) -> list[ShellContextContribution]
        # Return auth shell context.
    + def get_hooks(self) -> list[HookContribution]
        # Return auth lifecycle hooks.

## cli/doctor.py
  # CLI doctor checks for lexigram-auth.

+ def check_jwt_secret() -> dict[str, object]
    # Check JWT_SECRET env var or auth.jwt.secret config.

+ def check_auth_config() -> dict[str, object]
    # Validate auth section in application.yaml.

## cli/generators/auth_guard.py
  # Auth guard generator.

+ class AuthGuardGenerator:
    # Generator for authentication/authorization guards.
    + def generate(self, context: dict[str, object]) -> list[object]
        # Generate auth guard files.

## cli/generators/auth_policy.py
  # Auth policy generator.

+ class AuthPolicyGenerator:
    # Generator for authorization policies.
    + def generate(self, context: dict[str, object]) -> list[object]
        # Generate auth policy files.

## cli/generators/guard.py

+ class AuthGuardGenerator:
    + def generate(self, name: str, **options: Any) -> GenerationResult

## cli/hooks.py
  # CLI lifecycle hooks for lexigram-auth.

+ def log_auth_command(ctx: object) -> None
    # Audit-log auth-sensitive CLI commands.

## cli/shell.py
  # CLI shell context factories for lexigram-auth.

+ async def provide_auth(container: ContainerResolverProtocol) -> AuthenticationService
    # Provide AuthenticationService for interactive shell use.

## config.py
  # Configuration models for Lexigram Auth.

+ @dataclass(init=False)
+ class AuthUserConfig:
    # Single user configuration for bootstrapping.
    - @model_validator(mode='before')
    - def _handle_username(self, values: dict[str, Any]) -> dict[str, Any]

+ @dataclass(init=False)
+ class AuthRoleConfig:
    # Role configuration with permissions and inheritance.

+ @dataclass(init=False)
+ class RBACConfig:
    # RBAC system configuration.

+ @dataclass(init=False)
+ class JWTConfig:
    # JWT Configuration
    + @model_validator(mode='after')
    + def validate_jwt_security(self) -> JWTConfig
        # Enforce verified-only JWT policy based on deployment environment.

+ @dataclass(init=False)
+ class PasswordConfig:
    # Password complexity and validation configuration.

+ @dataclass(init=False)
+ class AuthMiddlewareConfig:
    # Configuration for authentication middleware.

+ @dataclass(init=False)
+ class AuthConfig:
    # Hierarchical root configuration for Lexigram Auth.
    + @model_validator(mode='after')
    + def validate_security(self) -> AuthConfig
        # Ensure secure settings in production.

## constants.py
  # Constants for lexigram-auth.

+ global ENV_PREFIX: str = 'LEX_AUTH__'

+ global ENV_NESTED_DELIMITER: str = '__'

+ global DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

+ global DEFAULT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

+ global DEFAULT_TOKEN_ALGORITHM: str = 'HS256'

+ global DEFAULT_TOKEN_TYPE: str = 'Bearer'

+ global DEFAULT_JWT_KEY_ROTATION_GRACE_PERIOD_SECONDS: int = 3600

+ global DEFAULT_MIN_PASSWORD_LENGTH: int = 8

+ global DEFAULT_MAX_PASSWORD_LENGTH: int = 128

+ global DEFAULT_PASSWORD_HASH_ROUNDS: int = 12

+ global DEFAULT_SESSION_TIMEOUT_MINUTES: int = 60

+ global DEFAULT_SESSION_COOKIE_NAME: str = 'session'

+ global DEFAULT_SESSION_COOKIE_SECURE: bool = True

+ global DEFAULT_SESSION_COOKIE_HTTPONLY: bool = True

+ global DEFAULT_TOTP_DIGITS: int = 6

+ global DEFAULT_TOTP_INTERVAL: int = 30

+ global DEFAULT_TOTP_VALID_WINDOW: int = 1

## decorators.py

- def _extract_request(*args: Any, **kwargs: Any) -> Any
    # Extract the request-like object from positional or keyword args.

+ def require_auth(fn: F) -> F
    # Require a valid authenticated identity on the request context.

+ def require_roles(*roles: str) -> Callable[, F]
    # Require that the authenticated identity holds at least one of the given roles.

+ global F

## di/bundle_provider.py
  # Convenience provider that registers the full authentication + authorisation stack.

+ class AuthBundleProvider:
    # Composite provider that wires the full Lexigram auth stack.
    __init__(self, config: AuthConfig | None = None, initial_roles: dict[str, Any] | None = None, enable_passkeys: bool = False, **kwargs: Any) -> None
    + def __init__(self, config: AuthConfig | None = None, initial_roles: dict[str, Any] | None = None, enable_passkeys: bool = False, **kwargs: Any) -> None
    + @classmethod
    + def from_config(cls, config: AuthConfig, **context: Any) -> Self
        # Create provider from config object.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register all auth sub-providers with the container.
    + async def boot(self, container: BootContainerProtocol) -> None
        # Boot all auth sub-providers in registration order.
    + async def shutdown(self) -> None
        # Shut down all auth sub-providers in reverse registration order.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Aggregate health check across all sub-providers.

## di/provider.py
  # DI provider for lexigram-auth.

+ class AuthProvider:
    # Authentication provider for Lexigram Framework.
    __init__(self, config: AuthConfig | None = None) -> None
    + def __init__(self, config: AuthConfig | None = None) -> None
    + @classmethod
    + def from_config(cls, config: AuthConfig, **context: Any) -> AuthProvider
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register auth services with the DI container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Boot the auth provider.
    + async def shutdown(self) -> None
        # Shutdown the auth provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Return health status of the auth provider.

## di/sub_providers/admin_provider.py
  # Admin DI provider: registers AuthAdminContributor.

+ class AuthAdminProvider:
    # Registers AuthAdminContributor for admin panel integration.
    __init__(self, config: AuthConfig | None = None) -> None
    + def __init__(self, config: AuthConfig | None = None) -> None
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Bind admin contributor singleton.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Boot the auth admin contributor.

## di/sub_providers/authentication_provider.py
  # Authentication provider - handles user authentication only.

+ @inject
+ class AuthenticationProvider:
    # User authentication ONLY (login/logout/validation).
    __init__(self, config: Annotated[AuthConfig, Inject] | None = None, password_policy: PasswordPolicy | None, user_store: UserStoreProtocol | None, token_manager: Any, cache_service: Any, mfa_service: MFAManager | None) -> None
    + def __init__(self, config: Annotated[AuthConfig, Inject] | None = None, password_policy: PasswordPolicy | None, user_store: UserStoreProtocol | None, token_manager: Any, cache_service: Any, mfa_service: MFAManager | None) -> None
    + @property
    + def service(self) -> AuthenticationService
        # Get or create the authentication service.
    + async def get_user(self, user_id: str) -> Any | None
        # Fetch a user by their ID.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register authentication services with the container.
    + async def boot(self, container: BootContainerProtocol) -> None
        # Initialize authentication provider and register with kernel health registry.
    + async def shutdown(self) -> None
        # Shutdown authentication provider.
    + async def verify_token(self, token: str) -> Result[VerifiedToken, TokenError]
        # Verify a JWT token and return a ``Result`` with the decoded payload.
    + async def validate_session(self, token: str) -> Any
        # Validate a session token and return user information.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check authentication provider health.

- def _build_token_manager(secret_key: str | None, jwt_algorithm: str, cache_service: Any, required_audience: str | None = None) -> Any
    # Build a JWTTokenManager from the supplied credentials.

## di/sub_providers/authorization_provider.py
  # Authorization provider - handles role-based access control and permissions.

+ @inject
+ class AuthorizationProvider:
    # Role-based access control and permission management.
    __init__(self, config: Annotated[AuthConfig, Inject] | None = None, initial_roles: dict[str, Any] | None = None, **kwargs: Any) -> None
    + def __init__(self, config: Annotated[AuthConfig, Inject] | None = None, initial_roles: dict[str, Any] | None = None, **kwargs: Any) -> None
    + @property
    + def auth_config(self) -> AuthConfig | None
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register authorization services with the container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize authorization provider.
    + async def shutdown(self) -> None
        # Shutdown authorization provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check authorization provider health.

## di/sub_providers/google_oauth_provider.py
  # Google OAuth provider — first-class Google token verification support.

+ @inject
+ class GoogleOAuthProvider:
    # Registers a first-class Google OAuth verification service.
    __init__(self, config: Annotated[AuthConfig, Inject] | None = None, google_oauth: dict[str, str] | None = None, http_client: Any | None = None, **kwargs: Any) -> None
    + def __init__(self, config: Annotated[AuthConfig, Inject] | None = None, google_oauth: dict[str, str] | None = None, http_client: Any | None = None, **kwargs: Any) -> None
    + @property
    + def service(self) -> GoogleOAuthService | None
        # Return the registered Google OAuth service, if any.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register the Google OAuth verifier service.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize Google OAuth support.
    + async def shutdown(self) -> None
        # Shutdown Google OAuth support.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check Google OAuth provider health.

## di/sub_providers/mfa_provider.py
  # MFA provider - handles multi-factor authentication only.

+ @inject
+ class MFAProvider:
    # Multi-factor authentication ONLY.
    __init__(self, **kwargs: Any) -> None
    + def __init__(self, **kwargs: Any) -> None
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register MFA services with the container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize MFA provider.
    + async def shutdown(self) -> None
        # Shutdown MFA provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check MFA provider health.

## di/sub_providers/oauth2_provider.py
  # OAuth2 provider - handles OAuth2/OIDC integration only.

+ @inject
+ class OAuth2Provider:
    # OAuth2/OIDC integration ONLY.
    __init__(self, config: Annotated[AuthConfig, Inject] | None = None, oauth2_providers: dict[str, dict[str, str]] | None = None, oauth_identity_store: OAuthIdentityStore | None = None, http_client: Any | None = None, **kwargs: Any) -> None
    + def __init__(self, config: Annotated[AuthConfig, Inject] | None = None, oauth2_providers: dict[str, dict[str, str]] | None = None, oauth_identity_store: OAuthIdentityStore | None = None, http_client: Any | None = None, **kwargs: Any) -> None
    + @property
    + def identity_resolver(self) -> OAuthIdentityStore | None
        # Return the OAuth identity store for resolving external IDs to internal UUIDs.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register OAuth2 services with the container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize OAuth2 provider.
    + async def shutdown(self) -> None
        # Shutdown OAuth2 provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check OAuth2 provider health.

## di/sub_providers/oauth_provider.py
  # OAuth provider config helpers for provider presets.

+ def detect_oauth_providers_from_config(oauth2_providers: dict[str, dict[str, str]]) -> dict[str, dict[str, str]]
    # Return valid OAuth2 providers from a pre-loaded config mapping.

## di/sub_providers/passkey_provider.py
  # Passkey provider - handles WebAuthn/Passkey support only.

+ @inject
+ class PasskeyProvider:
    # WebAuthn/Passkey support ONLY.
    __init__(self, **kwargs: Any) -> None
    + def __init__(self, **kwargs: Any) -> None
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register passkey services with the container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize passkey provider.
    + async def shutdown(self) -> None
        # Shutdown passkey provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check passkey provider health.

## di/sub_providers/session_provider.py
  # Session provider — registers ``SessionManagerImpl`` in the DI container.

+ class SessionProvider:
    # Registers :class:`~lexigram.auth.session.manager.SessionManagerImpl` in the container.
    __init__(self, config: Any = None, **kwargs: Any) -> None
    + def __init__(self, config: Any = None, **kwargs: Any) -> None
        # Initialise the session provider.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register :class:`SessionManagerImpl` as a singleton.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Boot the session provider.
    + async def shutdown(self) -> None
        # Shut down the session provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Return the health of the session subsystem.

## di/sub_providers/token_provider.py
  # Token management provider - handles JWT tokens only.

+ @inject
+ class TokenProvider:
    # JWT token management ONLY.
    __init__(self, config: Annotated[AuthConfig, Inject] | None = None, secret_key: str | None = None, jwt_algorithm: str | None = None, jwt_access_expiration_hours: int | None = None, jwt_refresh_expiration_days: int | None = None, **kwargs: Any) -> None
    + def __init__(self, config: Annotated[AuthConfig, Inject] | None = None, secret_key: str | None = None, jwt_algorithm: str | None = None, jwt_access_expiration_hours: int | None = None, jwt_refresh_expiration_days: int | None = None, **kwargs: Any) -> None
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register token services with the container.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Initialize token provider.
    + async def shutdown(self) -> None
        # Shutdown token provider.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check token provider health.

## events.py
  # Auth domain events emitted by key authentication operations.

+ @dataclass(frozen=True, init=False)
+ class UserAuthenticated:
    # Emitted when a user successfully authenticates.

+ @dataclass(frozen=True, init=False)
+ class AuthenticationFailed:
    # Emitted when an authentication attempt fails.

+ @dataclass(frozen=True, init=False)
+ class UserRegistered:
    # Emitted when a new user account is created.

+ @dataclass(frozen=True, init=False)
+ class PasswordChanged:
    # Emitted when a user successfully changes their password.

+ @dataclass(frozen=True, init=False)
+ class SessionCreated:
    # Emitted when a new session/token is issued.

+ @dataclass(frozen=True, init=False)
+ class SessionRevoked:
    # Emitted when a session/token is invalidated.

+ @dataclass(frozen=True, init=False)
+ class UserLoggedIn:
    # Emitted after a successful password-based login.

+ @dataclass(frozen=True, init=False)
+ class UserLoginFailed:
    # Emitted when a login attempt fails due to bad credentials.

+ @dataclass(frozen=True, init=False)
+ class UserLockedOut:
    # Emitted when a login attempt is rejected because the account is locked.

+ @dataclass(frozen=True, init=False)
+ class UserLoggedOut:
    # Emitted when a user explicitly logs out.

+ @dataclass(frozen=True, init=False)
+ class TokenRevoked:
    # Emitted when a specific token is revoked.

## exceptions.py
  # Exception hierarchy for Lexigram Auth.

+ class AuthError:
    # Base exception for all auth errors.

+ class AuthenticationError:
    # Raised when authentication fails.

+ class AuthorizationError:
    # Raised when user lacks required permissions.

+ class InvalidCredentialsError:
    # Raised when credentials are invalid.
    __init__(self, message: str = 'Invalid credentials', **kwargs: Any) -> None
    + def __init__(self, message: str = 'Invalid credentials', **kwargs: Any) -> 

+ class AccountLockedError:
    # Raised when an account is locked due to too many failed login attempts.
    __init__(self, email: str = '', **kwargs: Any) -> None
    + def __init__(self, email: str = '', **kwargs: Any) -> 

+ class UserNotFoundError:
    # Raised when user is not found.
    __init__(self, identifier: str, **kwargs: Any) -> None
    + def __init__(self, identifier: str, **kwargs: Any) -> 

+ class TokenError:
    # Base exception for token-related errors.

+ class InvalidTokenError:
    # Raised when a token is malformed or invalid.

+ class TokenExpiredError:
    # Raised when a token has expired.
    __init__(self, message: str = 'Token has expired', expiration_time: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Token has expired', expiration_time: str | None = None, **kwargs: Any) -> None

+ class TokenBlacklistedError:
    # Token has been explicitly revoked.
    __init__(self, message: str = 'Token has been revoked', **kwargs: Any) -> None
    + def __init__(self, message: str = 'Token has been revoked', **kwargs: Any) -> None

+ class TokenInvalidError:
    # Token is structurally invalid or has wrong type.
    __init__(self, message: str = 'Token is invalid', reason: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Token is invalid', reason: str | None = None, **kwargs: Any) -> None

+ class TokenAudienceError:
    # Token audience claim does not match expected.
    __init__(self, message: str = 'Token audience mismatch', expected: str | None = None, actual: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Token audience mismatch', expected: str | None = None, actual: str | None = None, **kwargs: Any) -> None

+ class TokenNotFoundError:
    # Token record does not exist.
    __init__(self, message: str = 'Token not found', token_id: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Token not found', token_id: str | None = None, **kwargs: Any) -> None

+ class InvalidAudienceError:
    # Raised when a token audience is invalid.

+ class InvalidScopeError:
    # Raised when a token lacks required scope.

+ class BlacklistedTokenError:
    # Raised when a token has been blacklisted.

+ class TokenExpiredVerificationError:
    # Account verification has expired.
    __init__(self, message: str = 'Verification has expired', user_id: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Verification has expired', user_id: str | None = None, **kwargs: Any) -> None

+ class AlreadyVerifiedError:
    # Account is already verified.
    __init__(self, message: str = 'Account is already verified', user_id: str | None = None, **kwargs: Any) -> None
    + def __init__(self, message: str = 'Account is already verified', user_id: str | None = None, **kwargs: Any) -> None

+ class EmailExistsError:
    # Raised when email is already taken.

+ class UsernameExistsError:
    # Raised when username is already taken.

+ class PasswordPolicyError:
    # Raised when password doesn't meet requirements.

+ class OAuth2Error:
    # Base exception for OAuth2 errors.

+ class SessionNotFoundError:
    # Raised when a session cannot be found in the store.
    __init__(self, session_id: str, **kwargs: Any) -> None
    + def __init__(self, session_id: str, **kwargs: Any) -> 

## hooks.py
  # Root hook payload surface for lexigram-auth.

+ @dataclass(frozen=True, kw_only=True)
+ class AuthUserAuthenticatedHook:
    # Payload fired when a user successfully authenticates.

+ @dataclass(frozen=True, kw_only=True)
+ class AuthAuthenticationFailedHook:
    # Payload fired when an authentication attempt fails.

+ @dataclass(frozen=True, kw_only=True)
+ class AuthTokenIssuedHook:
    # Payload fired when an access or refresh token is issued.

+ @dataclass(frozen=True, kw_only=True)
+ class AuthTokenRevokedHook:
    # Payload fired when a token is explicitly revoked.

+ @dataclass(frozen=True, kw_only=True)
+ class AuthTokenRefreshedHook:
    # Payload fired when an access token is refreshed.

## mfa/hooks.py
  # Lifecycle hooks for auth/mfa — intercepted when MFA operations occur.

+ @dataclass(frozen=True, kw_only=True)
+ class MFAChallengeIssuedHook:
    # Payload fired when an MFA challenge is issued to a user.

+ @dataclass(frozen=True, kw_only=True)
+ class MFAVerifiedHook:
    # Payload fired when MFA verification succeeds.

+ @dataclass(frozen=True, kw_only=True)
+ class MFAFailedHook:
    # Payload fired when MFA verification fails.

## mfa/manager.py
  # MFA Manager — consolidated TOTP and backup-code management.

+ @inject
+ class MFAManager:
    # Manages Multi-Factor Authentication (TOTP + backup codes) for users.
    __init__(self, user_store: UserStoreProtocol) -> None
    + def __init__(self, user_store: UserStoreProtocol) -> None
    + async def enable_totp(self, user_id: str, issuer: str = 'lexigram') -> tuple[str, str, list[str]]
        # Enable TOTP for a user and return enrollment credentials.
    + async def verify_totp(self, user_id: str, code: str) -> bool
        # Verify a TOTP or backup code for a user.
    + async def disable_totp(self, user_id: str) -> bool
        # Disable TOTP for a user.
    + def __repr__(self) -> str
        # Return a string representation of this MFAManager.

## mfa/totp_vectors.py
  # RFC 6238 TOTP test vectors for testing without pyotp.

+ @dataclass(frozen=True)
+ class TOTPTestVector:
    # A TOTP test vector from RFC 6238.

+ class TOTPTestVectors:
    # RFC 6238 test vectors for TOTP verification.
    + @classmethod
    + def get_all(cls) -> list[TOTPTestVector]
        # Get all test vectors.
    + @classmethod
    + def get_by_algorithm(cls, algorithm: str) -> list[TOTPTestVector]
        # Get test vectors by algorithm.
    + @classmethod
    + def get_by_digits(cls, digits: int) -> list[TOTPTestVector]
        # Get test vectors by digit count.

+ def generate_test_vector(secret: str, time: int, time_step: int = 30, digits: int = 6, algorithm: str = 'SHA1') -> str
    # Generate a TOTP for testing purposes.

## models/mfa.py
  # MFA model for Lexigram Auth.

+ @dataclass(frozen=True)
+ class UserMFA:
    # Represents MFA configuration for a user.

## models/session.py
  # Session model for Lexigram Auth.

+ @dataclass(frozen=True)
+ class UserSession:
    # User session data model.
    + def is_expired(self) -> bool
        # Return ``True`` if this session has passed its expiry time.
    + def is_valid(self) -> bool
        # Return ``True`` if the session is active and has not expired.
    + def remaining_ttl(self) -> timedelta | None
        # Return the time remaining until this session expires.
    + def refresh(self, expires_at: datetime, last_active_at: datetime | None = None) -> UserSession
        # Return a new :class:`UserSession` with an updated expiry time.

## models/token.py
  # Authentication token models.

+ @dataclass(init=False)
+ class AuthToken:
    # Authentication token response.
    token: str = Field(...)
    expires_at: datetime = Field(...)
    refresh_token: str | None = None
    refresh_expires_at: datetime | None = None
    token_type: str = Field(...)

## models/user.py
  # User model.

+ @dataclass(init=False)
+ class UserCredentials:
    # Sensitive credential data for a user.
    user_id: str = Field(...)
    hashed_password: str | None = None
    previous_hashes: list[str] = Field(default_factory=...)

+ @dataclass(init=False)
+ class User:
    # User model representing an authenticated user.
    user_id: str = Field(default_factory=...)
    email: str = ''
    name: str | None = None
    is_active: bool = True
    is_verified: bool = False
    is_superuser: bool = False
    roles: list[str] = Field(default_factory=...)
    permissions: list[str] = Field(default_factory=...)
    profile: dict[str, Any] = Field(default_factory=...)
    created_at: datetime | None = Field(default_factory=...)
    updated_at: datetime | None = Field(default_factory=...)
    last_login_at: datetime | None = None
    login_count: int = 0
    delegations: list[Any] = Field(default_factory=...)
    _request_metadata: dict[str, Any] = Field(default_factory=...)

## module.py
  # Authentication and authorization module for dependency injection.

+ @module(is_global=True)
+ class AuthModule:
    # Full authentication and authorization stack (JWT, OAuth2/OIDC, RBAC, policies).
    + @classmethod
    + def configure(cls, config: Any | None = None, initial_roles: dict[str, Any] | None = None, is_global: bool = True) -> DynamicModule
        # Create an AuthModule with explicit configuration.
    + @classmethod
    + def stub(cls, config: Any = None) -> DynamicModule
        # Return an in-memory AuthModule suitable for unit and integration testing.

## policies/engine.py
  # Policy Engine for ABAC evaluation.

+ class PatternMatcher:
    # Protocol for pattern matchers.
    + def can_match(self, pattern: str) -> bool ...
    + def matches(self, pattern: str, target: str) -> bool ...

+ class ExactPatternMatcher:
    # Matches exact string patterns without wildcards.
    + def can_match(self, pattern: str) -> bool
    + def matches(self, pattern: str, target: str) -> bool

+ class WildcardPatternMatcher:
    # Matches wildcard patterns using regex.
    + def can_match(self, pattern: str) -> bool
    + def matches(self, pattern: str, target: str) -> bool

+ class GlobPatternMatcher:
    # Matches glob-style patterns (e.g., 'user.*' matches 'user.read').
    + def can_match(self, pattern: str) -> bool
    + def matches(self, pattern: str, target: str) -> bool

+ class PatternMatcherRegistry:
    # Registry for pattern matchers.
    __init__(self) -> None
    + def __init__(self) -> None
    + @classmethod
    + def with_defaults(cls) -> PatternMatcherRegistry
        # Create a registry pre-loaded with the standard pattern matchers.
    - def _register_default_matchers(self) -> None
        # Register the default pattern matchers.
    + def register_matcher(self, matcher: PatternMatcher) -> None
        # Register a custom pattern matcher.
    + def matches(self, pattern: str, target: str) -> bool
        # Check if the target matches the pattern using registered matchers.

+ class PolicyEngine:
    # Evaluates authorization requests against a collection of policies.
    __init__(self, policies: list[Policy] | None = None, store: PolicyStoreProtocol | None, strategy: Literal['deny_first', 'allow_first', 'unanimous']) -> None
    + def __init__(self, policies: list[Policy] | None = None, store: PolicyStoreProtocol | None, strategy: Literal['deny_first', 'allow_first', 'unanimous']) -> None
        # Initialise the policy engine with a static list and/or a store.
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    - def _rebuild_resource_index(self) -> None
        # Rebuild the resource-pattern index from ``self.policies``.
    + async def load_from_store(self) -> None
        # Load policies from the configured :class:`PolicyStoreProtocol`.
    + async def save_policy(self, policy: Policy) -> None
        # Persist a policy to the store and add it to the in-memory list.
    + def evaluate(self, request: AuthorizationRequest) -> AuthorizationDecision
        # Evaluate an authorization request against loaded policies.
    - def _matches(self, policy: Policy, request: AuthorizationRequest) -> bool
        # Check if a policy applies to the given request.
    - def _pattern_match(self, patterns: list[str], target: str) -> bool
        # Check if target matches any of the patterns using the registry.

## policies/evaluator.py
  # Condition evaluators for ABAC Policy Engine.

+ class OperatorHandlerProtocol:
    # Protocol for operator handlers.
    + def compare(self, actual: Any, expected: Any) -> bool ...

+ class EqualsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class NotEqualsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class ContainsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class NotContainsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class InOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class NotInOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class MatchesOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class GreaterThanOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class LessThanOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class GreaterThanOrEqualsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class LessThanOrEqualsOperator:
    + def compare(self, actual: Any, expected: Any) -> bool

+ class OperatorRegistry:
    # Registry for condition operators.
    __init__(self) -> None
    + def __init__(self) -> None
    + @classmethod
    + def with_defaults(cls) -> OperatorRegistry
        # Create a registry pre-loaded with the standard operator handlers.
    - def _register_default_handlers(self) -> None
    + def register_handler(self, operator: str, handler: OperatorHandlerProtocol) -> None
        # Register a custom operator handler.
    + def compare(self, actual: Any, operator: str, expected: Any) -> bool
        # Compare using the registered handler for the operator.

+ class ConditionEvaluator:
    # Evaluates individual policy conditions against a request context.
    __init__(self) -> None
    + def __init__(self) -> None
    - @staticmethod
    - def _compile_path(path: str) -> Callable[, Any]
        # Compile an attribute path string into a reusable accessor function.
    + def evaluate(self, condition: Condition, context: dict[str, Any]) -> bool
        # Evaluate a single condition against the context.
    - def _resolve_attribute(self, path: str, context: dict[str, Any]) -> Any
        # Resolve a nested attribute from the context using a cached accessor.

## policies/in_memory_store.py
  # In-memory policy store for development and testing.

+ class InMemoryPolicyStore:
    # In-memory policy storage for development and testing.
    __init__(self) -> None
    + def __init__(self) -> None
    + async def get_all(self) -> list[Policy]
        # Get all policies.
    + async def get_by_id(self, policy_id: str) -> Policy | None
        # Get a policy by ID.
    + async def get_by_name(self, name: str) -> Policy | None
        # Get a policy by name.
    + async def save(self, policy: Policy) -> None
        # Save a policy.
    + async def delete(self, policy_id: str) -> bool
        # Delete a policy.
    + async def exists(self, policy_id: str) -> bool
        # Check if a policy exists.
    + def clear(self) -> None
        # Clear all policies.

## policies/store.py
  # Policy store protocols for ABAC policy persistence.

+ @runtime_checkable
+ class PolicyStoreProtocol:
    # Protocol for policy storage backends.

+ @runtime_checkable
+ class PolicyLoader:
    # Protocol for loading policies from various sources.

## policies/types.py
  # Core types for Lexigram ABAC Policy Engine.

+ class PolicyEffect:
    ALLOW = 'allow'
    DENY = 'deny'

+ class DecisionOutcome:
    ALLOW = 'allow'
    DENY = 'deny'
    INDETERMINATE = 'indeterminate'

+ @dataclass(frozen=True)
+ class Condition:
    # A condition that must be met for a policy to apply.

+ @dataclass(frozen=True)
+ class Policy:
    # A granular authorization policy.

+ @dataclass(frozen=True)
+ class AuthorizationRequest:
    # A request for authorization evaluation.

+ @dataclass(frozen=True)
+ class AuthorizationDecision:
    # The result of an authorization evaluation.

## protocols.py

+ @runtime_checkable
+ class TokenValidatorProtocol:
    # Validates and decodes authentication tokens.

+ @runtime_checkable
+ class IdentityResolverProtocol:
    # Resolves a token payload to a concrete user identity.

## services/result_pattern_service.py
  # Authentication service using Result pattern for error handling.

+ class AuthServiceWithResultPattern:
    # Authentication service using Result pattern.
    __init__(self, cache: CacheBackendProtocol | None = None, event_bus: EventBusProtocol | None = None) -> None
    + def __init__(self, cache: CacheBackendProtocol | None = None, event_bus: EventBusProtocol | None = None) -> None
        # Initialize the auth service with optional dependencies.
    + async def validate_password(self, password: str, min_length: int = 8, require_uppercase: bool = True, require_digits: bool = True) -> Result[None, AuthError]
        # Validate password against policy requirements.
    + async def verify_credentials(self, username: str, password: str, stored_hash: str | None = None) -> Result[bool, AuthError]
        # Verify user credentials against stored hash.
    + async def get_cached_token(self, token_id: str) -> Result[AuthToken | None, AuthError]
        # Get cached auth token.
    + async def cache_token(self, token_id: str, token: AuthToken, ttl: int = 3600) -> Result[None, AuthError]
        # Cache auth token with TTL.
    + async def invalidate_token(self, token_id: str) -> Result[None, AuthError]
        # Invalidate a cached token.

## session/cookie_backend.py
  # Session-cookie authentication backend for SSR admin flows.

+ class SessionCookieBackend:
    # Session-cookie authentication backend for SSR flows.
    __init__(self, session_repository: SessionRepositoryProtocol, user_fetcher: Callable[, Awaitable[AuthenticatedUserProtocol | None]], ids: IdGeneratorProtocol | None = None, cookie_name: str = 'session_id', secure: bool = True, http_only: bool = True, same_site: str = 'lax') -> None
    + def __init__(self, session_repository: SessionRepositoryProtocol, user_fetcher: Callable[, Awaitable[AuthenticatedUserProtocol | None]], ids: IdGeneratorProtocol | None = None, cookie_name: str = 'session_id', secure: bool = True, http_only: bool = True, same_site: str = 'lax') -> None
    + async def authenticate(self, request: Any) -> AuthenticatedUserProtocol | None
        # Extract session cookie, validate, return user or ``None``.
    + async def login(self, response: Any, user_id: str, expires_in: int = 86400) -> str
        # Create a session record and set the session cookie on *response*.
    + async def logout(self, request: Any, response: Any) -> None
        # Invalidate the session and clear the cookie.

## session/fingerprint.py
  # Device fingerprinting for Lexigram Auth.

+ def generate_device_id(fingerprint_data: dict[str, Any]) -> str
    # Generate a stable device ID from fingerprint data.

## session/hooks.py
  # Lifecycle hooks for auth/session — intercepted when session operations occur.

+ @dataclass(frozen=True, kw_only=True)
+ class SessionCreatedHook:
    # Payload fired when a new session is created.

+ @dataclass(frozen=True, kw_only=True)
+ class SessionRefreshedHook:
    # Payload fired when a session token is refreshed.

+ @dataclass(frozen=True, kw_only=True)
+ class SessionExpiredHook:
    # Payload fired when a session expires.

+ @dataclass(frozen=True, kw_only=True)
+ class SessionRevokedHook:
    # Payload fired when a session is explicitly revoked.

## session/manager.py
  # Session Management for Lexigram Auth.

+ @inject
+ class SessionManagerImpl:
    # Manages persistent user sessions with device awareness.
    __init__(self, session_store: SessionStore | None = None, ids: IdGeneratorProtocol | None = None, audit_logger: AuditLoggerProtocol | None, revoke_token: Callable[, Awaitable[None]] | None, max_sessions_per_user: int | None) -> None
    + def __init__(self, session_store: SessionStore | None = None, ids: IdGeneratorProtocol | None = None, audit_logger: AuditLoggerProtocol | None, revoke_token: Callable[, Awaitable[None]] | None, max_sessions_per_user: int | None) -> None
        # Initialise the session manager.
    + def __repr__(self) -> str
        # Return developer-friendly string representation.
    + async def create_session(self, user_id: str, fingerprint_data: dict[str, Any], ip_address: str | None = None, user_agent: str | None = None, expires_days: int = DEFAULT_EXPIRY_DAYS) -> UserSession
        # Create a new session for a user.
    + async def validate_session(self, session_id: str) -> Result[UserSession, AuthenticationError | SessionNotFoundError | TokenExpiredError]
        # Validate a session and update its activity.
    - def _prune_activity_write_cache(self, now: float) -> None
        # Remove stale entries from the activity-write tracker.
    + async def revoke_session(self, session_id: str) -> bool
        # Revoke a specific session.
    + async def verify_mfa(self, session_id: str) -> bool
        # Mark the session as MFA verified.
    + async def revoke_all_sessions(self, user_id: str) -> bool
        # Revoke all active sessions for a user.
    + async def get_active_sessions(self, user_id: str) -> list[UserSession]
        # List all active sessions for a user.
    - def _generate_fallback_id(self) -> str
        # Generate session ID when IdGenerator is not injected.

## storage/_mongo_store.py
  # MongoDB-backed user store implementation.

+ @inject
+ class MongoDBUserStore:
    # MongoDB-based user store using ``DocumentStoreProtocol``.
    __init__(self, document_store: DocumentStoreProtocol, collection_name: str = 'users') -> None
    + def __init__(self, document_store: DocumentStoreProtocol, collection_name: str = 'users') -> 
    - @property
    - def _col(self) -> CollectionProtocol
        # Lazily initialize the collection handle.
    - async def _ensure_collection(self) -> None
        # Ensure user collection exists.
    - async def _user_from_doc(self, doc: dict[str, Any]) -> User
        # Convert MongoDB document to User object.
    - async def _doc_from_user(self, user: User) -> dict[str, Any]
        # Convert User object to MongoDB document (non-credential fields).
    + async def create_user(self, name: str, email: str, hashed_password: str | None, roles: list[str] | None = None, permissions: list[str] | None = None, profile: dict[str, Any] | None = None, **kwargs: Any) -> User
        # Create a new user.
    + async def get_user_by_id(self, user_id: str) -> User | None
        # Get user by ID.
    + async def get_user_by_email(self, email: str) -> User | None
        # Get user by email.
    + async def update_user(self, user: User) -> None
        # Update non-credential user information.
    + async def delete_user(self, user_id: str) -> None
        # Delete a user.
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # List users with pagination.
    + async def count_users(self) -> int
        # Count total users.
    + async def get_credentials(self, user_id: str) -> UserCredentials | None
        # Return credential data for *user_id*.
    + async def update_credentials(self, creds: UserCredentials) -> None
        # Persist updated credentials for the user.

## storage/_sql_store.py
  # SQL-backed user store implementation.

+ @inject
+ class SQLUserStore:
    # Database-based user store (SQL-backed implementation)
    __init__(self, db_provider: DatabaseProviderProtocol) -> None
    + def __init__(self, db_provider: DatabaseProviderProtocol) -> 
    - async def _ensure_tables(self) -> None
        # Ensure user table exists (Managed by Alembic migrations).
    - async def _user_from_row(self, row: Any) -> User
        # Convert database row to User object
    - def _credentials_from_row(self, row: Any) -> UserCredentials
        # Extract credential data from a database row.
    + async def create_user(self, name: str, email: str, hashed_password: str, roles: list[str] | None = None, permissions: list[str] | None = None, profile: dict[str, Any] | None = None, **kwargs: Any) -> User
        # Create a new user using the canonical DatabaseProvider API.
    + async def get_user_by_id(self, user_id: str) -> User | None
        # Get user by ID
    + async def get_user_by_email(self, email: str) -> User | None
        # Get user by email
    + async def update_user(self, user: User) -> None
        # Update non-credential user information.
    + async def delete_user(self, user_id: str) -> None
        # Delete a user
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # List users with pagination
    + async def count_users(self) -> int
        # Count total users
    + async def get_credentials(self, user_id: str) -> UserCredentials | None
        # Return credential data for *user_id* from the database.
    + async def update_credentials(self, creds: UserCredentials) -> None
        # Persist updated credential data for ``creds.user_id``.

## storage/cached_user_store.py
  # Cached user store implementation for performance optimization

+ class CachedUserStore:
    # User store with multi-layer caching for high-performance user lookups.
    __init__(self, user_store: UserStoreProtocol, cache_service: CacheBackendProtocol, cache_ttl: int = 300, memory_cache_ttl: int = 60, pubsub: PubSubProtocol | None) -> None
    + def __init__(self, user_store: UserStoreProtocol, cache_service: CacheBackendProtocol, cache_ttl: int = 300, memory_cache_ttl: int = 60, pubsub: PubSubProtocol | None) -> 
        # Initialize cached user store.
    + async def subscribe_to_invalidations(self) -> None
        # Subscribe to cross-instance cache invalidation events.
    - async def _handle_invalidation(self, data: Any) -> None
        # Handle a ``user.cache.invalidate`` event from another instance.
    + async def get_user_by_id(self, user_id: str) -> User | None
        # Get user by ID with multi-layer caching.
    + async def get_user_by_email(self, email: str) -> User | None
        # Get user by email with caching.
    + async def update_user(self, user: User) -> None
        # Update user and invalidate all related caches.
    + async def delete_user(self, user_id: str) -> None
        # Delete user and invalidate caches.
    + async def create_user(self, name: str, email: str, hashed_password: str | None, roles: list[str] | None = None, permissions: list[str] | None = None, profile: dict[str, Any] | None = None, **kwargs: Any) -> User
        # Create user (no caching needed for new users).
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # List users (not cached for simplicity).
    + async def count_users(self) -> int
        # Count users (not cached for simplicity).
    + async def get_credentials(self, user_id: str) -> UserCredentials | None
        # Return credential data from the underlying store.
    + async def update_credentials(self, creds: UserCredentials) -> None
        # Persist updated credentials and invalidate the user cache.
    - def _serialize_user(self, user: User) -> dict[str, Any]
        # Serialize user for caching (credential fields excluded).
    - def _deserialize_user(self, data: dict[str, Any]) -> User
        # Deserialize user from cache (credential fields excluded).

+ global CACHE_INVALIDATION_TOPIC

## storage/db_stores.py
  # Database-backed user store implementations.

+ @inject
+ class RedisUserStore:
    # Redis-backed user cache (read-through cache, not primary storage).
    __init__(self, db_provider: DatabaseProviderProtocol, prefix: str = 'user:', ttl: int | None = None) -> None
    + def __init__(self, db_provider: DatabaseProviderProtocol, prefix: str = 'user:', ttl: int | None = None) -> None
    - async def _user_key(self, user_id: str) -> str
        # Generate Redis key for user
    - async def _user_from_data(self, data: dict[str, Any]) -> User
        # Convert Redis hash data to a User object (credentials excluded).
    - async def _data_from_user(self, user: User) -> dict[str, str]
        # Convert User object to Redis hash fields (non-credential fields only).
    + async def create_user(self, name: str, email: str, hashed_password: str | None, roles: list[str] | None = None, permissions: list[str] | None = None, profile: dict[str, Any] | None = None, **kwargs: Any) -> User
        # Cache a new user entry.
    + async def get_user_by_id(self, user_id: str) -> User | None
        # Get user by ID
    + async def get_user_by_email(self, email: str) -> User | None
        # Not supported — Redis does not index by email efficiently.
    + async def update_user(self, user: User) -> None
        # Update non-credential fields for the cached user entry.
    + async def delete_user(self, user_id: str) -> None
        # Delete a user
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # Not supported — Redis is not designed for full user enumeration.
    + async def count_users(self) -> int
        # Not supported — Redis is not designed for counting all users.
    + async def get_credentials(self, user_id: str) -> UserCredentials | None
        # Return cached credential data for *user_id*.
    + async def update_credentials(self, creds: UserCredentials) -> None
        # Update credential fields in the cached user hash.

## storage/in_memory_stores.py
  # In-memory session store for development and testing.

+ class InMemorySessionStore:
    # In-memory session storage for development and testing.
    __init__(self) -> None
    + def __init__(self) -> None
    + async def create(self, session: UserSession) -> str
        # Create a new session.
    + async def get(self, session_id: str) -> UserSession | None
        # Get a session by ID.
    + async def update(self, session_id: str, **updates: Any) -> None
        # Update session fields.
    + async def delete(self, session_id: str) -> bool
        # Delete a session.
    + async def delete_all_for_user(self, user_id: str) -> int
        # Delete all sessions for a user.
    + async def list_for_user(self, user_id: str) -> list[UserSession]
        # List all sessions for a user.

+ class InMemoryMFAStore:
    # In-memory MFA storage for development and testing.
    __init__(self) -> None
    + def __init__(self) -> None
    + async def get(self, user_id: str) -> dict[str, Any] | None
        # Get MFA config for a user.
    + async def save(self, mfa_data: dict[str, object]) -> None
        # Save MFA config for a user.
    + async def delete(self, user_id: str) -> bool
        # Delete MFA config for a user.

## storage/oauth_identity_store.py
  # OAuth identity storage for linking users to OAuth providers.

+ @runtime_checkable
+ class OAuthIdentityStore:
    # Protocol for OAuth identity storage.

+ class OAuthIdentity:
    # OAuth identity linking user to provider
    __init__(self, user_id: str, provider: str, provider_user_id: str, created_at: datetime | None = None, updated_at: datetime | None = None) -> None
    + def __init__(self, user_id: str, provider: str, provider_user_id: str, created_at: datetime | None = None, updated_at: datetime | None = None) -> 

+ @inject
+ class SQLAlchemyOAuthIdentityStore:
    # Database-backed OAuth identity store
    __init__(self, db_provider: DatabaseProviderProtocol) -> None
    + def __init__(self, db_provider: DatabaseProviderProtocol) -> 
    - async def _ensure_tables(self) -> None
        # Ensure oauth_identities table exists.
    - async def _identity_from_row(self, row: Any) -> OAuthIdentity
        # Convert database row to OAuthIdentity object
    + async def create_oauth_identity(self, user_id: str, provider: str, provider_user_id: str) -> OAuthIdentity
        # Create OAuth identity link
    + async def get_oauth_identity(self, provider: str, provider_user_id: str) -> OAuthIdentity | None
        # Get OAuth identity by provider and provider user ID
    + async def get_oauth_identities_for_user(self, user_id: str) -> list[OAuthIdentity]
        # Get all OAuth identities for a user
    + async def delete_oauth_identity(self, provider: str, provider_user_id: str) -> bool
        # Delete OAuth identity
    + async def delete_oauth_identities_for_user(self, user_id: str) -> int
        # Delete all OAuth identities for a user
    + async def get_user_by_oauth_identity(self, provider: str, provider_user_id: str) -> str | None
        # Get local user_id by OAuth provider and external user ID.
    + async def resolve_user_id(self, user_id_or_oauth_id: str, provider: str = 'google') -> str | None
        # Resolve user_id from either UUID or OAuth external ID.
    + def resolve_user_id_sync(self, external_id: str, provider: str = 'google') -> str | None
        # Synchronous resolution is not supported for database-backed store.

+ @inject
+ class MongoDBOAuthIdentityStore:
    # MongoDB-backed OAuth identity store
    __init__(self, db_provider: DatabaseProviderProtocol, collection_name: str = 'oauth_identities') -> None
    + def __init__(self, db_provider: DatabaseProviderProtocol, collection_name: str = 'oauth_identities') -> 
    - async def _ensure_collection(self) -> None
        # Ensure collection exists with indexes
    - async def _identity_from_doc(self, doc: dict[str, Any]) -> OAuthIdentity
        # Convert MongoDB document to OAuthIdentity object
    - async def _doc_from_identity(self, identity: OAuthIdentity) -> dict[str, Any]
        # Convert OAuthIdentity object to MongoDB document
    + async def create_oauth_identity(self, user_id: str, provider: str, provider_user_id: str) -> OAuthIdentity
        # Create OAuth identity link
    + async def get_oauth_identity(self, provider: str, provider_user_id: str) -> OAuthIdentity | None
        # Get OAuth identity by provider and provider user ID
    + async def get_oauth_identities_for_user(self, user_id: str) -> list[OAuthIdentity]
        # Get all OAuth identities for a user
    + async def delete_oauth_identity(self, provider: str, provider_user_id: str) -> bool
        # Delete OAuth identity
    + async def delete_oauth_identities_for_user(self, user_id: str) -> int
        # Delete all OAuth identities for a user
    + async def get_user_by_oauth_identity(self, provider: str, provider_user_id: str) -> str | None
        # Get local user_id by OAuth provider and external user ID.
    + async def resolve_user_id(self, user_id_or_oauth_id: str, provider: str = 'google') -> str | None
        # Resolve user_id from either UUID or OAuth external ID.
    + def resolve_user_id_sync(self, external_id: str, provider: str = 'google') -> str | None
        # Synchronous resolution is not supported for database-backed store.

## storage/session_store.py
  # Session store protocols for abstracting session storage.

+ @runtime_checkable
+ class SessionStore:
    # Protocol for session storage backends.

+ @runtime_checkable
+ class MFAStore:
    # Protocol for MFA storage backends.

## storage/token_store.py
  # User and token storage interfaces and implementations

+ @runtime_checkable
+ class CachedUserStore:
    # Protocol for read-through cache user stores (point-lookup only).

+ @runtime_checkable
+ class UserStoreProtocol:
    # Protocol for user storage implementations.

+ class InMemoryUserStore:
    # Simple in-memory user store for development/testing
    __init__(self) -> None
    + def __init__(self) -> None
    + async def create_user(self, name: str, email: str, hashed_password: str | None, roles: list[str] | None = None, permissions: list[str] | None = None, profile: dict[str, Any] | None = None, **kwargs: Any) -> User
        # Create a new user
    + async def get_user_by_id(self, user_id: str) -> User | None
        # Get user by ID
    + async def get_user_by_email(self, email: str) -> User | None
        # Get user by email
    + async def get_user_by_username(self, username: str) -> User | None
        # Get user by username (name).
    + async def update_user(self, user: User) -> None
        # Update user information
    + async def delete_user(self, user_id: str) -> None
        # Delete a user
    + async def list_users(self, skip: int = 0, limit: int = 100) -> list[User]
        # List users with pagination
    + async def count_users(self) -> int
        # Count total users
    + async def get_credentials(self, user_id: str) -> UserCredentials | None
        # Return stored credentials for *user_id*.
    + async def update_credentials(self, creds: UserCredentials) -> None
        # Persist updated credentials for the user.

## types.py
  # Type definitions for Lexigram Auth.

+ class AuthStatus:
    # Authentication status values.
    AUTHENTICATED = 'authenticated'
    UNAUTHENTICATED = 'unauthenticated'
    TOKEN_EXPIRED = 'token_expired'
    TOKEN_INVALID = 'token_invalid'
    USER_INACTIVE = 'user_inactive'
    USER_NOT_VERIFIED = 'user_not_verified'

+ class TokenType:
    # Token type values.
    BEARER = 'Bearer'
    BASIC = 'Basic'
    API_KEY = 'ApiKey'

+ class UserStatus:
    # User account status values.
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'
    PENDING_VERIFICATION = 'pending_verification'
    DELETED = 'deleted'

+ @dataclass(init=False)
+ class GuardContext:
    # Context passed to authorization guards.
    user: User | None = None
    request: Any | None = None
    request_context_user_id: str | None = None
    route: str | None = None
    method: str | None = None
    path: str | None = None
    headers: dict[str, str] = Field(default_factory=...)
    params: dict[str, Any] = Field(default_factory=...)

+ @dataclass(init=False)
+ class AuthResult:
    # Result of an authentication attempt.
    success: bool = Field(...)
    status: AuthStatus = Field(...)
    user: User | None = None
    token: AuthToken | None = None
    message: str | None = None

+ @dataclass(init=False)
+ class OAuth2UserInfo:
    # User information returned by an OAuth2 provider.
    provider: str = Field(...)
    provider_user_id: str = Field(...)
    email: str | None = None
    username: str | None = None
    name: str | None = None
    avatar_url: str | None = None
    raw_data: dict[str, Any] | None = None

+ @dataclass(init=False)
+ class RoleDefinition:
    # Definition of a role with its permissions.
    name: str = Field(...)
    description: str = ''
    permissions: list[str] = Field(default_factory=...)
    inherits: list[str] = Field(default_factory=...)

+ @dataclass(init=False)
+ class AuthHealthResult:
    # Health check result for auth components.
    status: HealthStatus = Field(...)
    message: str = Field(...)
    users_count: int = 0
    components: dict[str, dict[str, Any]] = Field(default_factory=...)

+ @dataclass(frozen=True)
+ class TokenPair:
    # A minimal access + refresh token pair.

## web/guards.py
  # GuardProtocol services for authorization in Lexigram Framework

- class _GuardBase:
    # Private abstract base for auth guards; provides default handle_rejection.
    + @abstractmethod
    + async def can_activate(self, context: GuardContext) -> bool
        # Check if the guard allows the request to proceed
    + async def handle_rejection(self, context: GuardContext) -> ResponseProtocol
        # Handle guard rejection by returning appropriate response.

+ class AuthGuard:
    # GuardProtocol that requires authentication
    + async def can_activate(self, context: GuardContext) -> bool
        # Check if user is authenticated
    + async def handle_rejection(self, context: GuardContext) -> ResponseProtocol
        # Return 401 for unauthenticated requests.

+ class RoleGuard:
    # GuardProtocol that requires specific roles
    __init__(self, *roles: str) -> None
    + def __init__(self, *roles: str) -> None
    + async def can_activate(self, context: GuardContext) -> bool
        # Check if user has required roles

+ class PermissionGuard:
    # GuardProtocol that requires specific permissions
    __init__(self, *permissions: str) -> None
    + def __init__(self, *permissions: str) -> None
    + async def can_activate(self, context: GuardContext) -> bool
        # Check if user has required permissions

+ class CompositeGuard:
    # GuardProtocol that combines multiple guards with AND logic
    __init__(self, *guards: GuardProtocol) -> None
    + def __init__(self, *guards: GuardProtocol) -> None
    + async def can_activate(self, context: GuardContext) -> bool
        # Check if all guards pass

+ class AdminGuard:
    # GuardProtocol that requires admin role
    __init__(self) -> None
    + def __init__(self) -> None

+ class UserGuard:
    # GuardProtocol that requires any authenticated user

+ class GuardFactory:
    # Factory for creating guards via dependency injection.
    + @classmethod
    + async def get_guard(cls, guard_type: type[GuardProtocol], resolver: Any | None = None) -> GuardProtocol
        # Get a guard instance, resolving from DI container if needed.

- def _get_request_resolver(request: Any) -> Any | None

- async def _get_request_context_user_id(request: Any) -> str | None

+ def use_guards(*guards: GuardProtocol) -> Callable[, Callable[..., Any]]
    # Apply guards to a route handler (auth-scoped internal implementation).

+ def require_auth() -> Callable[, Callable[..., Any]]
    # Decorator requiring authentication.

+ def require_admin() -> Callable[, Callable[..., Any]]
    # Decorator requiring admin role.

+ def require_role(*roles: str) -> Callable[, Callable[..., Any]]
    # Decorator requiring specific roles

+ def require_permission(*permissions: str) -> Callable[, Callable[..., Any]]
    # Decorator requiring specific permissions

## web/middleware/auth.py
  # Authentication middleware for web applications

+ class AuthMiddleware:
    # Middleware for handling authentication and authorization - Pure ASGI implementation.
    __init__(self, auth_provider: AuthProviderProtocol, config: AuthMiddlewareConfig | None = None, ctx: Context | None = None, attempt_tracker: LoginAttemptTracker | None = None) -> None
    + def __init__(self, auth_provider: AuthProviderProtocol, config: AuthMiddlewareConfig | None = None, ctx: Context | None = None, attempt_tracker: LoginAttemptTracker | None = None) -> 
    + def should_skip_auth(self, path: str) -> bool
        # Check if authentication should be skipped for this path
    + def extract_token(self, request: Request) -> str | None
        # Extract authentication token from request
    + async def authenticate_request(self, request: Any) -> User | None
        # Authenticate the request and return user if valid
    + def check_authorization(self, user: User) -> bool
        # Check if user is authorized based on roles/permissions
    + async def __call__(self, scope: dict[str, Any], receive: Callable, send: Callable) -> None
        # Pure ASGI middleware entry point - OPT-AUTH-2.
    + def set_app(self, app: Callable) -> None
        # Set the ASGI app to wrap.

+ class AuthRouter:
    # Router extension with authentication helpers
    __init__(self, auth_provider: AuthProviderProtocol) -> None
    + def __init__(self, auth_provider: AuthProviderProtocol) -> 
    + def require_auth(self, roles: list[str] | None = None, permissions: list[str] | None = None, optional: bool = False) -> Callable[, Callable[..., Any]]
        # Decorator to require authentication and authorization for routes
    + def get_current_user(self, request: Request) -> User | None
        # Get current authenticated user from request

- def _extract_request(*args: Any, **kwargs: Any) -> Any
    # Extract the Starlette-like request object from positional or keyword args.

- async def _get_auth_provider(context: Any | None = None) -> AuthProviderProtocol
    # Resolve `AuthProvider` from dynamic context or global container.

- async def _get_response_factory(context: Any | None = None) -> Any
    # Resolve `ResponseFactoryProtocol` from global container.

+ def require_mfa(max_age_seconds: int = 300) -> Callable[, Callable[..., Any]]
    # Decorator to require MFA verification (step-up).

## web/middleware/jwt_authenticator.py
  # JWT token authentication component.

+ class JwtAuthenticator:
    # Handles JWT token validation and user resolution.
    __init__(self, auth_provider: AuthProviderProtocol, config = None, logger: Logger | None = None) -> None
    + def __init__(self, auth_provider: AuthProviderProtocol, config = None, logger: Logger | None = None) -> 
    + async def authenticate(self, request: Any) -> Any | None
        # Validate JWT token from request and return user if valid.

## web/middleware/response_handler.py

+ class AuthResponseHandler:
    # Handles authentication-related HTTP responses.
    + @staticmethod
    + async def unauthorized_response(message: str = 'Authentication required', request: Any = None, response_factory: Any | None = None) -> Any
        # Return 401 Unauthorized response or redirect to login.
    + @staticmethod
    + async def forbidden_response(message: str = 'Insufficient permissions', request: Any | None = None, response_factory: Any | None = None) -> Any
        # Return 403 Forbidden response.

- async def _get_response_factory(context: Any | None = None) -> Any
    # Resolve `ResponseFactoryProtocol` from context or global container.

## web/middleware/session_authenticator.py
  # Session-based authentication component.

+ class SessionAuthenticator:
    # Handles session validation and user resolution.
    __init__(self, auth_provider: AuthProviderProtocol) -> None
    + def __init__(self, auth_provider: AuthProviderProtocol) -> 
    + async def authenticate(self, request: Any) -> Any
        # Validate session from cookies and return user if valid.

## web/middleware/session_validator.py
  # Session validation utilities for authentication middleware.

+ class SessionValidator:
    # Handles session validation and authorization checks.
    __init__(self, config: Any, auth_provider: Any) -> None
    + def __init__(self, config: Any, auth_provider: Any) -> None
        # Initialize with configuration and auth provider.
    + def check_authorization(self, user: User) -> bool
        # Check if user is authorized based on roles/permissions.
    + def should_skip_auth(self, path: str) -> bool
        # Check if authentication should be skipped for this path.

## web/middleware/throttle.py
  # Rate-limiting middleware for authentication endpoints.

+ class RateLimitExceededError:
    # Raised when a client has exceeded the configured rate limit.
    __init__(self, retry_after: int) -> None
    + def __init__(self, retry_after: int) -> None

+ class RateLimitMiddleware:
    # ASGI middleware that rate-limits authentication endpoints.
    __init__(self, app: Any, rate_limit: str = '5/minute', block_duration: int = 60, paths: frozenset[str] | None = None, cache_service: Any | None = None) -> None
    + def __init__(self, app: Any, rate_limit: str = '5/minute', block_duration: int = 60, paths: frozenset[str] | None = None, cache_service: Any | None = None) -> None
    + async def __call__(self, scope: dict[str, Any], receive: Any, send: Any) -> None
        # Process an ASGI request.
    - @staticmethod
    - async def _send_429(send: Any, retry_after: int) -> None
        # Send a 429 Too Many Requests ASGI response.

- def _parse_rate_limit(rate_limit: str) -> tuple[int, int]
    # Parse a rate-limit string such as ``"5/minute"`` into ``(max, seconds)``.

+ def throttle(rate_limit: str = '5/minute', block_duration: int = 60, paths: frozenset[str] | None = None) -> Callable[, RateLimitMiddleware]
    # Decorator / factory that wraps an ASGI app with :class:`RateLimitMiddleware`.

## web/middleware/token_cache.py
  # Token caching utilities for authentication middleware.

+ class TokenCache:
    # Cache for JWT tokens with LRU eviction and TTL support.
    __init__(self, max_size: int = 10000, ttl_seconds: float = 300.0, cache_backend: CacheBackendProtocol | None = None) -> None
    + def __init__(self, max_size: int = 10000, ttl_seconds: float = 300.0, cache_backend: CacheBackendProtocol | None = None) -> 
        # Initialize token cache.
    - def _cleanup_expired(self) -> None
        # Remove expired entries from cache.
    - def _evict_if_needed(self) -> None
        # Evict oldest entry if cache is full.
    + async def get(self, token: str) -> Any | None
        # Get cached user for token, or None if not cached/expired.
    + async def set(self, token: str, user: Any) -> None
        # Cache user for token.
    + async def invalidate(self, token: str) -> None
        # Invalidate a specific token from cache.
    + def clear(self) -> None
        # Clear all cached tokens.
    + def stats(self) -> dict[str, Any]
        # Get cache statistics.

## web/middleware/token_extractor.py
  # Token extraction utilities for authentication middleware.

+ class TokenExtractor:
    # Handles extraction of authentication tokens from HTTP requests.
    __init__(self, config: Any) -> None
    + def __init__(self, config: Any) -> None
        # Initialize with middleware configuration.
    + def extract_token(self, request: Request) -> str | None
        # Extract authentication token from request.