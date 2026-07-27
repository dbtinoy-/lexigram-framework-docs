---
title: Lexigram-Cache API
description: Lexigram-Cache API guide and reference for the lexigram-cache package in the Lexigram framework.
---

## __init__.py
  # Lexigram Cache - Multi-backend caching system for Lexigram Framework.

- def __getattr__(name: str) -> Any

- def __dir__() -> Any

## admin/contributor.py
  # Admin contributor for lexigram-cache — surfaces cache hit/miss, eviction,

+ class CacheAdminContributor:
    # Admin contributor for the lexigram-cache package.
    __init__(self) -> None
    + def __init__(self) -> None
    + async def on_admin_boot(self, container: ContainerResolverProtocol) -> None
        # Resolve cache admin dependencies from the DI container.
    + def get_routes(self) -> Sequence[AdminRouteSpec]
    + def get_dashboard_widgets(self) -> Sequence[DashboardWidgetDefinition]
    + def get_navigation_items(self) -> Sequence[NavigationContribution]
    + def get_health_definitions(self) -> Sequence[AdminHealthDefinition]
    + def get_actions(self) -> Sequence[AdminActionDefinition]
    + async def render_widget(self, widget_name: str, params: WidgetParams) -> Result[WidgetViewModel, AdminError]
        # Render a named widget using registry dispatch.

- async def _empty_handler(request: object) -> str
    # Placeholder handler for contributed routes.

## admin/handlers/backend_ping.py
  # Backend ping widget handler.

+ class BackendPingWidgetHandler:
    # Pings the cache backend.
    __init__(self, cache: CacheBackendProtocol) -> None
    + def __init__(self, cache: CacheBackendProtocol) -> None
    + async def get_data(self, params: WidgetParams) -> Result[BackendPingViewModel, AdminError]
        # Perform a health check on the cache backend.

## admin/handlers/eviction_rate.py
  # Eviction rate widget handler.

+ class EvictionRateWidgetHandler:
    # Fetches cache eviction rate.
    __init__(self, cache: CacheBackendProtocol) -> None
    + def __init__(self, cache: CacheBackendProtocol) -> None
    + async def get_data(self, params: WidgetParams) -> Result[EvictionRateViewModel, AdminError]
        # Fetch cache eviction stats.

## admin/handlers/hit_miss_ratio.py
  # Hit/miss ratio widget handler.

+ class HitMissRatioWidgetHandler:
    # Fetches cache hit/miss ratio.
    __init__(self, cache: CacheBackendProtocol) -> None
    + def __init__(self, cache: CacheBackendProtocol) -> None
    + async def get_data(self, params: WidgetParams) -> Result[HitMissRatioViewModel, AdminError]
        # Fetch cache hit/miss stats.

## admin/renderer.py
  # Shared Jinja2 renderer for lexigram-cache admin widgets.

+ class PackageWidgetRenderer:
    # Renders admin widget templates for lexigram-cache. Singleton.
    __init__(self) -> None
    + def __init__(self) -> None
    + def render(self, template_name: str, context: dict[str, Any]) -> str
        # Render a template. Raises jinja2.TemplateNotFound on misconfiguration.

## admin/viewmodels.py
  # Frozen view models for lexigram-cache admin widgets.

+ @dataclass(frozen=True)
+ class HitMissRatioViewModel:
    # View data for cache hit/miss ratio widget.

+ @dataclass(frozen=True)
+ class EvictionRateViewModel:
    # View data for cache eviction rate widget.

+ @dataclass(frozen=True)
+ class BackendPingViewModel:
    # View data for cache backend ping widget.

## backends/factory.py
  # Backend factory helpers for Lexigram Cache provider.

+ async def create_backend(config: CacheBackendConfig, container: Any | None = None, hooks: HookRegistryProtocol | None = None) -> CacheBackendProtocol
    # Create a backend instance from a CacheBackendConfig.

## backends/hash.py
  # Cache key hashing utilities.

- def _compute_hash(data: str, algorithm: str = 'blake2b') -> str
    # Compute hash for cache key derivation.

## backends/memcached/backend.py
  # Memcached cache backend implementation.

+ class MemcachedCacheBackend:
    # Memcached cache backend implementation.
    __init__(self, servers: list[str], config: CacheOperationConfig | None = None) -> None
    + def __init__(self, servers: list[str], config: CacheOperationConfig | None = None) -> 
        # Initialize the Memcached cache backend.
    - async def _get_client(self) -> AsyncMemcachedClient
        # Lazy client initialization.
    + async def get(self, key: str) -> Any | None
        # Get a value from the cache.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> bool
        # Set a value in the cache with optional TTL.
    + async def delete(self, key: str) -> bool
        # Delete a value from the cache.
    + async def exists(self, key: str) -> bool
        # Check if a key exists in the cache.
    + async def clear(self) -> bool
        # Clear all values from the cache.
    + async def get_many(self, keys: list[str]) -> dict[str, Any]
        # Get multiple values from the cache.
    + async def set_many(self, items: dict[str, Any], ttl: int | None = None) -> bool
        # Set multiple values in the cache.
    + async def delete_many(self, keys: list[str]) -> bool
        # Delete multiple values from the cache.
    + async def delete_pattern(self, pattern: str) -> int
        # Delete keys matching a pattern.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Perform a health check on the cache backend.

## backends/memory/backend.py
  # Memory cache backend implementation using lexigram-components.

+ class MemoryCacheBackend:
    # Memory cache backend using lexigram-components MemoryStateStore.
    __init__(self, config: CacheOperationConfig | None = None, max_size: int | None = None, hooks: HookRegistryProtocol | None = None) -> None
    + def __init__(self, config: CacheOperationConfig | None = None, max_size: int | None = None, hooks: HookRegistryProtocol | None = None) -> None
        # Initialize the memory cache backend.
    - async def _emit_action(self, hook_name: str, payload: object) -> None
        # Emit a cache action hook when a registry is available.
    + async def get(self, key: str) -> Result[Any | None, CacheError]
        # Get a value from the cache.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> Result[None, CacheError]
        # Set a value in the cache with optional TTL.
    + async def delete(self, key: str) -> Result[bool, CacheError]
        # Delete a value from the cache.
    + async def exists(self, key: str) -> Result[bool, CacheError]
        # Check if a key exists in the cache.
    + async def clear(self) -> Result[None, CacheError]
        # Clear all values from the cache.
    + async def get_many(self, keys: list[str]) -> Result[dict[str, Any], CacheError]
        # Get multiple values from the cache.
    + async def set_many(self, items: dict[str, Any], ttl: int | None = None) -> Result[None, CacheError]
        # Set multiple values in the cache.
    + async def delete_many(self, keys: list[str]) -> Result[int, CacheError]
        # Delete multiple values from the cache.
    + async def delete_pattern(self, pattern: str) -> Result[int, CacheError]
        # Delete all keys matching a glob-style pattern.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Perform a health check on the cache backend.

## backends/memory/kv.py
  # In-memory storage implementation for Lexigram.

+ class InMemoryStorage:
    # Namespace-aware in-memory storage backend backed by MemoryStateStore.
    __init__(self, max_size: int = 10000, default_ttl: int | None = None, cleanup_interval: int = 60) -> None
    + def __init__(self, max_size: int = 10000, default_ttl: int | None = None, cleanup_interval: int = 60) -> 
    + @property
    + def storage_type(self) -> StorageType
    - def _get_store(self, namespace: str) -> MemoryStateStore
        # Return (or create) the MemoryStateStore for *namespace*.
    + async def connect(self) -> None
    + async def disconnect(self) -> None
    + async def get(self, key: str, namespace: str | None = None) -> Any | None
    + async def set(self, key: str, value: Any, namespace: str | None = None, ttl: int | None = None) -> bool
    + async def delete(self, key: str, namespace: str | None = None) -> bool
    + async def exists(self, key: str, namespace: str | None = None) -> bool
    + async def list_keys(self, pattern: str | None = None, namespace: str | None = None) -> list[str]
    + async def clear(self, namespace: str | None = None) -> bool
    - async def _periodic_cleanup(self) -> None
    - async def _cleanup_expired(self) -> None
    + def get_stats(self) -> dict[str, Any]
        # Return basic statistics about memory usage.

## backends/memory_lock.py
  # In-memory lock store implementation

+ class MemoryLockStore:
    # In-memory lock store for testing
    __init__(self) -> None
    + def __init__(self) -> None
    + async def is_locked(self, key: str) -> bool
        # Check if a key is locked
    + async def acquire(self, lock_name: str, owner: str, ttl: int) -> bool
        # Attempt to acquire a lock.
    + async def release(self, lock_name: str, owner: str) -> bool
        # Release a lock.
    - async def _cleanup_expired(self, key: str) -> None
        # Remove expired lock for a single key (internal helper).
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the lock store

## backends/memory_secrets.py
  # In-memory secret store implementation

+ class MemorySecretStore:
    # In-memory secret store for testing
    __init__(self, secrets: dict[str, str] | None = None) -> None
    + def __init__(self, secrets: dict[str, str] | None = None) -> 
    + async def get_secret(self, key: str) -> str | None
        # Get a secret by name
    + async def set_secret(self, key: str, value: str) -> None
        # Set a secret
    + async def delete_secret(self, key: str) -> None
        # Delete a secret
    + async def list_secrets(self, prefix: str | None = None) -> list[str]
        # List secrets with optional prefix
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the secret store

## backends/memory_state.py
  # In-memory state store implementation

+ class MemoryStateStore:
    # In-memory state store with optional LRU eviction.
    __init__(self, max_size: int | None = None) -> None
    + def __init__(self, max_size: int | None = None) -> None
        # Initialise the state store.
    - def _serialize_value(self, value: Any) -> bytes
        # Serialize value to JSON bytes with enhanced type support.
    - def _deserialize_value(self, value: bytes) -> Any
        # Deserialize value from JSON bytes.
    - def _evict_expired(self) -> None
        # Remove all expired entries in-place (single pass, no allocation).
    + async def get(self, key: str) -> Any | None
        # Get a value by key, touching it as most-recently-used.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> bool
        # Set a value with optional TTL, evicting the LRU entry if at capacity.
    + async def delete(self, key: str) -> bool
        # Delete a value by key.
    + async def exists(self, key: str) -> bool
        # Check if a key exists and has not expired.
    + async def clear(self) -> None
        # Clear all values from the store.
    + async def get_bulk(self, keys: list[str]) -> dict[str, Any]
        # Get multiple values by keys.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the state store.

## backends/redis/backend.py
  # Redis cache backend implementation using the centralized StateStoreProtocol protocol.

+ class RedisCacheBackend:
    # Redis cache backend using StateStoreProtocol protocol.
    __init__(self, store: StateStoreProtocol, config: CacheOperationConfig | None = None, hooks: HookRegistryProtocol | None = None) -> None
    + def __init__(self, store: StateStoreProtocol, config: CacheOperationConfig | None = None, hooks: HookRegistryProtocol | None = None) -> 
        # Initialize the Redis cache backend.
    + def get_underlying_client(self) -> Any | None
        # Return the underlying Redis client for app.state integration.
    - async def _emit_action(self, hook_name: str, payload: object) -> None
        # Emit a cache action hook when a registry is available.
    + async def get(self, key: str) -> Result[Any | None, CacheError]
        # Get a value from the cache.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> Result[None, CacheError]
        # Set a value in the cache with optional TTL.
    + async def delete(self, key: str) -> Result[bool, CacheError]
        # Delete a value from the cache.
    + async def exists(self, key: str) -> Result[bool, CacheError]
        # Check if a key exists in the cache.
    + async def clear(self) -> Result[None, CacheError]
        # Clear all values from the cache.
    + async def get_many(self, keys: list[str]) -> Result[dict[str, Any], CacheError]
        # Get multiple values from the cache.
    + async def set_many(self, items: dict[str, Any], ttl: int | None = None) -> Result[None, CacheError]
        # Set multiple values in the cache using pipeline.
    + async def delete_many(self, keys: list[str]) -> Result[int, CacheError]
        # Delete multiple values from the cache using pipeline.
    + async def delete_pattern(self, pattern: str) -> Result[int, CacheError]
        # Delete all Redis keys matching a glob-style pattern.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Perform a health check on the cache backend.

## backends/redis/circuit.py
  # Local circuit breaker backend types for lexigram-cache.

+ @dataclass
+ class CircuitBreakerState:
    # Serialized circuit breaker state for distributed storage.
    name: str
    state: CircuitState
    failure_count: int
    success_count: int
    last_failure_time: float | None
    last_success_time: float | None
    last_state_change: float

+ class CircuitBreakerBackend:
    # Protocol for circuit breaker state backends.

## backends/redis/resilience.py
  # Resilience backends for the Lexigram cache package.

+ class RedisCircuitBreakerBackend:
    # Redis backend for distributed circuit breaker state.
    __init__(self, redis_url: str = 'redis://localhost:6379', key_prefix: str = 'lexigram:cb:', ttl: int = 3600) -> None
    + def __init__(self, redis_url: str = 'redis://localhost:6379', key_prefix: str = 'lexigram:cb:', ttl: int = 3600) -> None
    - async def _get_redis(self) -> Any
        # Lazy-initialise the Redis client.
    + async def get_state(self, name: str) -> CircuitBreakerState | None
        # Return circuit breaker state stored in Redis, or ``None``.
    + async def set_state(self, name: str, state: CircuitBreakerState) -> None
        # Persist circuit breaker *state* under *name* in Redis.
    + async def delete_state(self, name: str) -> None
        # Remove the stored state for *name* from Redis.

## backends/redis/resilient.py
  # Resilient Redis cache backend — decorator composition (D3.3).

+ class ResilientRedisCacheBackend:
    # Composes a ``CacheBackendProtocol`` with a ``CircuitBreakerProtocol``.
    __init__(self, inner: CacheBackendProtocol, breaker: CircuitBreakerProtocol) -> None
    + def __init__(self, inner: CacheBackendProtocol, breaker: CircuitBreakerProtocol) -> None
    + async def get(self, key: str) -> Any
        # Get a value — routed through the circuit breaker.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> Any
        # Set a value — routed through the circuit breaker.
    + async def delete(self, key: str) -> Any
        # Delete a value — routed through the circuit breaker.
    + async def exists(self, key: str) -> Any
        # Check existence — routed through the circuit breaker.
    + async def clear(self) -> Any
        # Clear all keys — routed through the circuit breaker.
    + async def get_many(self, keys: list[str]) -> Any
    + async def set_many(self, items: dict[str, Any], ttl: int | None = None) -> Any
    + async def delete_many(self, keys: list[str]) -> Any
    + async def delete_pattern(self, pattern: str) -> Any
    + async def health_check(self, timeout: float = 5.0) -> Any

## backends/registry.py
  # Cache backend registry for extensible cache backends.

+ class CacheBackendRegistry:
    # Protocol for cache backend factories.
    + def can_create(self, backend_type: str) -> bool ...
    + def create_backend(self, **kwargs: Any) -> Any ...

+ class MemoryBackendRegistry:
    # Registry for memory cache backend.
    + def can_create(self, backend_type: str) -> bool
    + def create_backend(self, **kwargs: Any) -> Any

+ class RedisBackendRegistry:
    # Registry for Redis cache backend.
    + def can_create(self, backend_type: str) -> bool
    + def create_backend(self, **kwargs: Any) -> Any

+ class MemcachedBackendRegistry:
    # Registry for Memcached cache backend.
    + def can_create(self, backend_type: str) -> bool
    + def create_backend(self, **kwargs: Any) -> Any

+ class BackendRegistry:
    # Central registry for all cache backends.
    __init__(self) -> None
    + def __init__(self) -> None
        # Initialise with all built-in backend factories.
    - def _register_defaults(self) -> None
        # Populate built-in factories under their type-string keys.
    + def register(self, registry_or_key: CacheBackendRegistry | str, value: Any = None) -> None
        # Register a backend factory.
    + def get_backend(self, backend_type: str, **kwargs: Any) -> Any
        # Return a backend instance for *backend_type*.

## cli/checks.py
  # CLI health checks for lexigram-cache.

+ async def check_cache_connection(container: ContainerResolverProtocol) -> dict[str, object]
    # Verify cache backend connectivity.

## cli/commands.py
  # Cache CLI command group factory.

+ def create_cache_app() -> typer.Typer
    # Create the `lexigram cache` command group.

## cli/contributor.py
  # Cache CLI contributor definitions.

+ class CacheCliContributor:
    # CLI contributor for the lexigram-cache package.
    + @property
    + def contributor_id(self) -> str
        # Return the contributor identifier.
    + def get_generators(self) -> list[GeneratorDefinition]
        # Return generator definitions for cache.
    + def get_commands(self) -> list[CommandContribution]
        # Return the contributed `cache` command group.
    + def get_health_checks(self) -> list[HealthCheckContribution]
        # Return cache connectivity health check.
    + def get_doctor_checks(self) -> list[DoctorCheckContribution]
        # Return cache configuration doctor checks.
    + def get_shell_context(self) -> list[ShellContextContribution]
        # Return cache shell context.
    + def get_hooks(self) -> list
        # Return no hook contributions.

## cli/doctor.py
  # CLI doctor checks for lexigram-cache.

+ def check_cache_configured() -> dict[str, object]
    # Check cache backend is configured.

## cli/generators/cache_repository.py
  # Cache repository generator for creating cached data repositories.

+ class CacheRepositoryGenerator:
    # Generator for creating cached repositories.
    __init__(self, output_dir: str | Path = 'src/repositories') -> None
    + def __init__(self, output_dir: str | Path = 'src/repositories') -> None
    + def generate(self, name: str, output_dir: str | Path | None, fields_str: str | None, dry_run: bool, force: bool, **options: Any) -> GenerationResult
        # Generate a cached repository.
    - @staticmethod
    - def _derive_pk(fields: list[FieldSpec]) -> tuple[str, str]
        # Derive the primary-key name and type from the field list.

## cli/shell.py
  # CLI shell context factories for lexigram-cache.

+ async def provide_cache(container: ContainerResolverProtocol) -> CacheBackend
    # Provide cache backend for interactive shell use.

## config.py
  # Consolidated cache configuration.

+ @dataclass(init=False)
+ class CacheOperationConfig:
    # Internal configuration for cache operations. Shared across backends.
    default_ttl: int | None = Field(...)
    max_memory: int | None = Field(...)
    key_prefix: str = Field(...)
    enable_metrics: bool = Field(...)
    serializer_type: str = Field(...)

+ @dataclass(init=False)
+ class MemoryBackendConfig:
    # Configuration for in-memory cache backend.
    name: str = Field(...)
    default: bool = Field(...)
    enabled: bool = Field(...)
    default_ttl: int | None = Field(...)
    max_size: int | None = Field(...)
    cleanup_interval: int = Field(...)
    key_prefix: str = Field(...)

+ @dataclass(init=False)
+ class RedisBackendConfig:
    # Configuration for Redis cache backend.
    name: str = Field(...)
    default: bool = Field(...)
    enabled: bool = Field(...)
    host: str = Field(...)
    port: int = Field(...)
    db: int = Field(...)
    password: str | None = Field(...)
    url: str | None = Field(...)
    default_ttl: int | None = Field(...)
    key_prefix: str = Field(...)
    ssl: bool = Field(...)
    connection_pool_size: int = Field(...)
    socket_timeout: float = Field(...)
    retry_on_timeout: bool = Field(...)

+ @dataclass(init=False)
+ class MemcachedBackendConfig:
    # Configuration for Memcached cache backend.
    name: str = Field(...)
    default: bool = Field(...)
    enabled: bool = Field(...)
    host: str = Field(...)
    port: int = Field(...)
    servers: list[str] | None = Field(...)
    default_ttl: int | None = Field(...)
    key_prefix: str = Field(...)
    connect_timeout: float = Field(...)
    timeout: float = Field(...)
    max_pool_size: int = Field(...)

+ @dataclass(init=False)
+ class CacheBackendConfig:
    # Unified (flattened-union) configuration for any single cache backend.
    name: str = Field(...)
    type: BackendType = Field(...)
    default: bool = Field(...)
    enabled: bool = Field(...)
    default_ttl: int | None = Field(...)
    key_prefix: str = Field(...)
    enable_metrics: bool = Field(...)
    health_check_interval: int = Field(...)
    max_size: int | None = Field(...)
    cleanup_interval: int = Field(...)
    redis_host: str = Field(...)
    redis_port: int = Field(...)
    redis_db: int = Field(...)
    redis_password: str | None = Field(...)
    redis_url: str | None = Field(...)
    redis_ssl: bool = Field(...)
    redis_pool_size: int = Field(...)
    memcached_host: str = Field(...)
    memcached_port: int = Field(...)
    memcached_servers: list[str] | None = Field(...)

+ @dataclass(init=False)
+ class CacheServiceConfig:
    # Configuration for the cache service layer.
    enable_protection: bool = Field(...)
    enable_metrics: bool = Field(...)
    enable_health_checks: bool = Field(...)
    protection_lock_ttl: int = Field(...)
    protection_max_wait: float = Field(...)
    protection_retry_interval: float = Field(...)
    default_backend: str | None = Field(...)
    circuit_breaker_enabled: bool = Field(...)
    circuit_breaker_threshold: int = Field(...)
    allow_pickle: bool = Field(...)
    default_serializer: str = Field(...)

+ @dataclass(init=False)
+ class CacheConfig:
    # Top-level configuration for Lexigram Cache.
    + @property
    + def is_production(self) -> bool
        # Check if running in production environment.
    + @property
    + def is_development(self) -> bool
        # Check if running in development environment.
    + @property
    + def is_test(self) -> bool
        # Check if running in test environment.
    + @model_validator(mode='after')
    + def validate_production_security(self) -> CacheConfig
        # Block insecure cache configurations in production.
    + @field_validator('backends')
    + @classmethod
    + def validate_default_backend(cls, v: list[CacheBackendConfig]) -> list[CacheBackendConfig]
        # Ensure exactly one default backend is specified.
    + @field_validator('backends')
    + @classmethod
    + def validate_unique_names(cls, v: list[CacheBackendConfig]) -> list[CacheBackendConfig]
        # Ensure backend names are unique.
    + def get_default_backend(self) -> CacheBackendConfig | None
        # Get the default backend configuration.
    + def get_backend(self, name: str) -> CacheBackendConfig | None
        # Get a backend configuration by name.
    + @classmethod
    + def get_provider_class(cls) -> type
        # Return the provider class for this config.

+ class EnvironmentConfigLoader:
    # Loader for cache configuration from various sources.
    + @staticmethod
    + def from_env(prefix: str = const.ENV_PREFIX) -> CacheConfig
        # Load CacheConfig from environment variables.
    + @staticmethod
    + def from_dict(config_dict: dict[str, Any]) -> CacheConfig
        # Load CacheConfig from a dictionary.
    + @staticmethod
    + def from_yaml(file_path: str) -> CacheConfig
        # Load CacheConfig from a YAML file.
    + @staticmethod
    + def from_json(file_path: str) -> CacheConfig
        # Load CacheConfig from a JSON file.

+ def get_backend_type_from_string(type_str: str) -> BackendType
    # Convert string to BackendType using registry lookup.

+ def default_cache_config() -> CacheOperationConfig
    # Factory for default cache operation configuration.

+ def make_cache_config(**kwargs: Any) -> CacheConfig
    # Helper to create cache config from kwargs.

+ def make_cache_service_config(**kwargs: Any) -> CacheServiceConfig
    # Helper to create service config from kwargs.

+ global BACKEND_TYPE_MAP: dict[str, BackendType]

## constants.py
  # Cache constants for lexigram-cache.

+ global ENV_PREFIX: str = 'LEX_CACHE__'

+ global ENV_NESTED_DELIMITER: str = '__'

+ global ENV_VAR_LEX_ENV: str = 'LEX_ENV'

+ global DEFAULT_CACHE_NAME: str = 'cache'

+ global DEFAULT_CACHE_VERSION: str = '1.0.0'

+ global DEFAULT_CACHE_ENABLED: bool = True

+ global DEFAULT_CACHE_ENVIRONMENT: str = 'development'

+ global DEFAULT_CACHE_DEBUG: bool = False

+ global DEFAULT_SERVICE_PROTECTION_ENABLED: bool = True

+ global DEFAULT_SERVICE_METRICS_ENABLED: bool = True

+ global DEFAULT_SERVICE_HEALTH_CHECKS_ENABLED: bool = True

+ global DEFAULT_SERVICE_CIRCUIT_BREAKER_ENABLED: bool = False

+ global DEFAULT_SERVICE_CIRCUIT_BREAKER_THRESHOLD: int = 5

+ global DEFAULT_SERVICE_SERIALIZER: str = 'json'

+ global DEFAULT_SERVICE_ALLOW_PICKLE: bool = False

+ global DEFAULT_PROTECTION_LOCK_TTL: int = 30

+ global DEFAULT_PROTECTION_MAX_WAIT: float = 10.0

+ global DEFAULT_PROTECTION_RETRY_INTERVAL: float = 0.1

+ global DEFAULT_MEMORY_NAME: str = 'memory'

+ global DEFAULT_MEMORY_ENABLED: bool = True

+ global DEFAULT_MEMORY_DEFAULT: bool = False

+ global DEFAULT_MEMORY_CLEANUP_INTERVAL: int = 60

+ global DEFAULT_REDIS_NAME: str = 'redis'

+ global DEFAULT_REDIS_HOST: str = 'localhost'

+ global DEFAULT_REDIS_PORT: int = 6379

+ global DEFAULT_REDIS_DB: int = 0

+ global DEFAULT_REDIS_ENABLED: bool = True

+ global DEFAULT_REDIS_DEFAULT: bool = False

+ global DEFAULT_REDIS_SSL: bool = False

+ global DEFAULT_REDIS_CONNECTION_POOL_SIZE: int = 10

+ global DEFAULT_REDIS_SOCKET_TIMEOUT: float = 5.0

+ global DEFAULT_REDIS_RETRY_ON_TIMEOUT: bool = True

+ global DEFAULT_MEMCACHED_NAME: str = 'memcached'

+ global DEFAULT_MEMCACHED_HOST: str = 'localhost'

+ global DEFAULT_MEMCACHED_PORT: int = 11211

+ global DEFAULT_MEMCACHED_ENABLED: bool = True

+ global DEFAULT_MEMCACHED_DEFAULT: bool = False

+ global DEFAULT_LOCK_KEY_PREFIX: str = 'lock:'

+ global DEFAULT_LOCK_TTL: int = 30

+ global DEFAULT_LOCK_RENEWAL_INTERVAL_DIVISOR: int = 2

+ global COMPRESSION_MARKER_UNCOMPRESSED: bytes = b'\x00'

+ global COMPRESSION_MARKER_COMPRESSED: bytes = b'\x01'

+ global DEFAULT_COMPRESSION_THRESHOLD: int = 1024

+ global DEFAULT_COMPRESSION_LEVEL: int = 6

+ global INSECURE_PASSWORDS: tuple[str, ...]

+ global BACKEND_TYPE_MEMORY: str = 'memory'

+ global BACKEND_TYPE_REDIS: str = 'redis'

+ global BACKEND_TYPE_MEMCACHED: str = 'memcached'

+ global CACHE_STATUS_HIT: str = 'hit'

+ global CACHE_STATUS_MISS: str = 'miss'

+ global CACHE_STATUS_SET: str = 'set'

+ global CACHE_STATUS_DELETE: str = 'delete'

+ global CACHE_STATUS_ERROR: str = 'error'

+ global CACHE_STATUS_EXPIRED: str = 'expired'

+ global CACHE_STATUS_STALE: str = 'stale'

+ global ERROR_MSG_CACHE_TIMEOUT: str = 'Cache operation timed out'

+ global ERROR_MSG_CACHE_CONFIGURATION: str = 'Cache configuration error'

+ global ERROR_MSG_CACHE_STAMPEDE: str = 'Cache stampede protection error'

+ global ERROR_MSG_CACHE_INVALIDATION: str = 'Cache invalidation failed'

+ global ERROR_MSG_REDIS_INSTALL: str = 'Redis backend requires redis package. Install with: pip install lexigram-cache[redis]'

+ global ERROR_MSG_MEMCACHED_INSTALL: str = 'Memcached backend requires pylibmc or python-memcached. Install with: pip install lexigram-cache[memcached]'

+ global ERROR_MSG_PYYAML_INSTALL: str = 'PyYAML is required for YAML configuration loading'

+ global ERROR_MSG_INSECURE_PASSWORD: str = "CRITICAL SECURITY ERROR: Insecure {backend} password detected in PRODUCTION for backend '{name}'.\nYou MUST set a secure password via {env_var}."

+ global ERROR_MSG_INSECURE_URL: str = "CRITICAL SECURITY ERROR: Insecure {backend} URL detected in PRODUCTION for backend '{name}'.\nYou MUST set a secure {backend} URL via {env_var}."

+ global DEFAULT_ENCODING: str = 'utf-8'

## decorators.py

- def _is_domain_model(obj: Any) -> bool
    # Return True if *obj* supports the model_dump / model_validate protocol.

- def _serialize(value: Any) -> Any
    # Prepare *value* for JSON-safe cache storage.

- def _deserialize(value: Any) -> Any
    # Reconstruct *value* from a cache-retrieved payload.

+ def cacheable(ttl: int | None = 300, key_prefix: str = '', skip_on_error: bool = True) -> Callable[, F]
    # Cache the return value of an async method using the injected CacheBackend.

+ global F

## di/provider.py
  # Integration layer for Lexigram Cache provider.

+ class CacheProvider:
    # Lexigram Cache provider for lexigram integration.
    __init__(self, config: CacheConfig | None = None) -> None
    + def __init__(self, config: CacheConfig | None = None) -> None
        # Initialize the cache provider.
    + @classmethod
    + def from_config(cls, config: CacheConfig, **context: Any) -> CacheProvider
        # Create a CacheProvider from a CacheConfig.
    + def configure(self, config: dict[str, Any] | CacheConfig) -> None
        # Configure the provider with cache settings.
    + async def register(self, container: ContainerRegistrarProtocol) -> None
        # Register cache services with the container.
    - async def _discover_backends(self, container: ContainerRegistrarProtocol) -> None
        # Scan the ``lexigram.cache.backends`` entry-point group.
    + async def boot(self, container: ContainerResolverProtocol) -> None
        # Start the cache provider.
    + def observe_repository(self, cache_repository: Any, repository: Any) -> None
        # Queue cache repository observation wiring for provider boot.
    + async def shutdown(self) -> None
        # Shutdown the cache provider and cleanup resources.
    + @property
    + def cache(self) -> CacheService
        # Get the default cache service.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check provider health.
    - def _initialize_serializers(self) -> None
        # Initialize available serializers.
    - async def _initialize_backends(self, container: ContainerResolverProtocol | None = None) -> None
        # Initialize configured cache backends.
    - async def _create_backend(self, config: CacheBackendConfig, container: ContainerResolverProtocol | None = None) -> CacheBackendProtocol
        # Create a backend instance from configuration.
    - def _initialize_services(self) -> None
        # Initialize cache services for each backend.
    - def _create_service(self, backend_name: str, backend: CacheBackendProtocol) -> CacheService
        # Create a cache service for a backend.
    + def get_service(self, backend_name: str | None = None) -> CacheService
        # Get a cache service by backend name.
    + def get_backend(self, backend_name: str | None = None) -> Any
        # Get a backend instance by name.
    + def get_default_service(self) -> CacheService
        # Get the default cache service.
    + async def get_health_status(self) -> HealthCheckResult
        # Return comprehensive health status of all cache services and backends.
    + async def get_metrics(self) -> dict[str, Any]
        # Return comprehensive metrics from all registered cache services.
    - def _register_semantic_cache(self, container: ContainerRegistrarProtocol) -> None
        # Register semantic cache components if faiss is available.
    - @staticmethod
    - def _faiss_available() -> bool
        # Check if faiss package is installed.
    - def _register_admin_components(self, container: ContainerRegistrarProtocol) -> None
        # Register admin widget renderer and contributor.

- def __getattr__(name: str) -> Any
    # Lazy-load heavy symbols that are only needed at runtime.

+ global T

## events.py
  # Domain events for cache subsystem.

+ @dataclass(frozen=True)
+ class CacheHitEvent:
    # Cache lookup resulted in a hit.

+ @dataclass(frozen=True)
+ class CacheMissEvent:
    # Cache lookup resulted in a miss.

+ @dataclass(frozen=True)
+ class CacheEvictedEvent:
    # Cache entry was evicted.

+ @dataclass(frozen=True)
+ class CacheConnectedEvent:
    # Cache backend connection established.

## exceptions.py
  # Cache exceptions module.

+ class CacheError:
    # Base exception for cache errors.

+ class CacheBackendError:
    # Raised when the cache backend (Redis/Memcached) fails.

+ class CacheConnectionError:
    # Raised when the cache connection fails.

+ class CacheTimeoutError:
    # Raised when a cache operation times out.
    __init__(self, message: str = const.ERROR_MSG_CACHE_TIMEOUT, key: str | None = None, backend: str | None = None, timeout_seconds: float | None = None, **kwargs) -> None
    + def __init__(self, message: str = const.ERROR_MSG_CACHE_TIMEOUT, key: str | None = None, backend: str | None = None, timeout_seconds: float | None = None, **kwargs) -> 

+ class CacheKeyError:
    # Raised when a cache key is invalid or for key-specific errors.

+ class CacheConfigurationError:
    # Raised when cache configuration is invalid.
    __init__(self, message: str = const.ERROR_MSG_CACHE_CONFIGURATION, setting: str | None = None, value: Any | None = None, **kwargs) -> None
    + def __init__(self, message: str = const.ERROR_MSG_CACHE_CONFIGURATION, setting: str | None = None, value: Any | None = None, **kwargs) -> 

+ class CacheStampedeError:
    # Raised when cache stampede protection fails.
    __init__(self, message: str = const.ERROR_MSG_CACHE_STAMPEDE, lock_holder: str | None = None, **kwargs) -> None
    + def __init__(self, message: str = const.ERROR_MSG_CACHE_STAMPEDE, lock_holder: str | None = None, **kwargs) -> 

+ class CacheInvalidationError:
    # Raised when cache invalidation fails.
    __init__(self, message: str = const.ERROR_MSG_CACHE_INVALIDATION, keys: list[str] | None = None, tag: str | None = None, pattern: str | None = None, **kwargs) -> None
    + def __init__(self, message: str = const.ERROR_MSG_CACHE_INVALIDATION, keys: list[str] | None = None, tag: str | None = None, pattern: str | None = None, **kwargs) -> 

+ class LockAcquisitionError:
    # Raised when a distributed lock cannot be acquired.

+ class CacheSerializationError:
    # Raised when serialization/deserialization fails.

+ class CacheCapacityError:
    # Raised when the cache is at capacity.

## hooks.py
  # Root hook payload surface for lexigram-cache.

+ @dataclass(frozen=True, kw_only=True)
+ class CacheConnectedHook:
    # Payload fired when the cache backend establishes its connection.

+ @dataclass(frozen=True, kw_only=True)
+ class CacheDisconnectedHook:
    # Payload fired when the cache backend disconnects or is shut down.

+ @dataclass(frozen=True, kw_only=True)
+ class CacheHitHook:
    # Payload fired when a cache lookup returns a stored value.

+ @dataclass(frozen=True, kw_only=True)
+ class CacheMissHook:
    # Payload fired when a cache lookup does not find a stored value.

+ @dataclass(frozen=True, kw_only=True)
+ class CacheEntryEvictedHook:
    # Payload fired when a cache entry is evicted (TTL expiry or explicit removal).

## locks/auto_renewing.py

+ class AutoRenewingLock:
    # Distributed lock with automatic TTL renewal.
    __init__(self, redis: Any, key: str, lock_id: str, ttl: int, auto_renew: bool = True, renew_interval: int | None = None) -> None
    + def __init__(self, redis: Any, key: str, lock_id: str, ttl: int, auto_renew: bool = True, renew_interval: int | None = None) -> None
        # Initialize auto-renewing lock.
    + async def start_auto_renewal(self) -> None
        # Start background task to auto-renew lock.
    + async def stop_auto_renewal(self) -> None
        # Stop background renewal task.
    - async def _renewal_loop(self) -> None
        # Background loop to renew lock TTL.
    - async def _extend_lock(self) -> bool
        # Extend lock TTL using Lua script.
    + async def release(self) -> None
        # Release lock and stop auto-renewal.

## locks/context.py

+ class LockContextManager:
    # Async context manager for distributed locks.
    __init__(self, redis: Any, key: str, ttl: int, auto_renew: bool) -> None
    + def __init__(self, redis: Any, key: str, ttl: int, auto_renew: bool) -> None
    + async def __aenter__(self) -> AutoRenewingLock
    + async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: object) -> None

## locks/distributed.py
  # Distributed lock with automatic TTL renewal.

+ class DistributedLockProtocol:
    # Distributed lock with automatic TTL renewal.
    __init__(self, redis_client, key: str, ttl: int = const.DEFAULT_LOCK_TTL, renewal_interval: int | None = None) -> None
    + def __init__(self, redis_client, key: str, ttl: int = const.DEFAULT_LOCK_TTL, renewal_interval: int | None = None) -> None
        # Initialize distributed lock.
    + async def acquire(self) -> bool
        # Try to acquire the lock.
    + async def release(self) -> bool
        # Release the lock.
    - def _on_renewal_done(self, task: asyncio.Task[None]) -> None
        # Callback invoked when the renewal task finishes.
    - async def _renew_lock(self) -> None
        # Background task to renew lock periodically.
    + @asynccontextmanager
    + async def lock(self) -> 
        # Async context manager for lock acquisition.
    + @property
    + def is_locked(self) -> bool
        # Check if this instance currently holds the lock.
    + @property
    + def lock_info(self) -> DistributedLockInfo | None
        # Get lock ownership information.

## locks/manager.py
  # Manager for distributed locks.

+ class LockManager:
    # Manager for distributed locks.
    __init__(self, redis_client, default_ttl: int = const.DEFAULT_LOCK_TTL) -> None
    + def __init__(self, redis_client, default_ttl: int = const.DEFAULT_LOCK_TTL) -> None
        # Initialize lock manager.
    + def create_lock(self, key: str, ttl: int | None = None) -> DistributedLockProtocol
        # Create distributed lock.
    + async def release_all(self) -> None
        # Release all managed locks.

## module.py
  # Cache module for dependency injection.

+ @module(is_global=True)
+ class CacheModule:
    # Redis and in-memory cache backends with stampede protection.
    + @classmethod
    + def configure(cls, config: Any | None = None) -> DynamicModule
        # Create a CacheModule with explicit configuration.
    + @classmethod
    + def stub(cls, config: Any = None) -> DynamicModule
        # Return an in-memory CacheModule for unit testing.

## protocols.py
  # Cache protocols module.

+ @runtime_checkable
+ class CacheProviderProtocol:
    # Protocol for cache providers.
    + def get_backend(self, name: str | None = None) -> CacheBackendProtocol ...

+ @runtime_checkable
+ class CacheHealthCheckProtocol:
    # Protocol for cache health checkers.

+ @runtime_checkable
+ class CacheKeyBuilderProtocol:
    # Protocol for cache key builders.
    + def build_key(self, prefix: str, *args: Any, **kwargs: Any) -> str ...

+ @runtime_checkable
+ class CacheProtectionStrategyProtocol:
    # Protocol for cache protection strategies.

+ @runtime_checkable
+ class CacheSerializerProtocol:
    # Cache-specific protocol for value serializers.
    + def serialize(self, value: Any) -> bytes | str ...
    + def deserialize(self, data: bytes | str) -> Any ...

## repository/base.py
  # RepositoryProtocol pattern implementations for Lexigram Cache.

+ class CacheRepository:
    # Base class for cache repositories.
    __init__(self, cache_service: CacheService, namespace: str, default_ttl: int | None = None) -> None
    + def __init__(self, cache_service: CacheService, namespace: str, default_ttl: int | None = None) -> 
        # Initialize the repository.
    - def _make_key(self, key: K) -> str
        # Create a namespaced cache key.
    + async def get(self, key: K) -> T | None
        # Get an item from cache.
    + async def set(self, key: K, value: T, ttl: int | None = None) -> bool
        # Set an item in cache.
    + async def delete(self, key: K) -> bool
        # Delete an item from cache.
    + async def exists(self, key: K) -> bool
        # Check if an item exists in cache.
    + async def get_or_set(self, key: K, default_func: Callable[, T], ttl: int | None = None) -> T
        # Get an item or compute and cache it.
    + async def invalidate_pattern(self, pattern: str) -> None
        # Invalidate all keys matching a pattern.

+ class EntityRepository:
    # RepositoryProtocol for caching domain entities.
    __init__(self, cache_service: CacheService, entity_type: str, default_ttl: int | None = None, key_field: str = 'id') -> None
    + def __init__(self, cache_service: CacheService, entity_type: str, default_ttl: int | None = None, key_field: str = 'id') -> 
        # Initialize entity repository.
    - def _make_entity_key(self, entity: dict[str, Any] | object) -> str
        # Create cache key from entity.
    + async def get_by_id(self, entity_id: K) -> T | None
        # Get entity by ID.
    + async def save(self, entity: T, ttl: int | None = None) -> bool
        # Save entity to cache.
    + async def delete_by_id(self, entity_id: K) -> bool
        # Delete entity by ID.
    + async def invalidate(self, entity_id: K) -> bool
        # Invalidate the cached entity by ID.
    + async def invalidate_by_entity(self, entity: T) -> bool
        # Invalidate the cache entry for *entity* by extracting its key.
    + def observe(self, repository: AbstractRepository) -> None
        # Wire automatic cache invalidation hooks into a repository.
    + async def get_multiple(self, entity_ids: list[K]) -> dict[K, T]
        # Get multiple entities by IDs.
    + async def save_multiple(self, entities: list[T], ttl: int | None = None) -> bool
        # Save multiple entities to cache.

+ class QueryRepository:
    # RepositoryProtocol for caching query results.
    __init__(self, cache_service: CacheService, query_type: str, default_ttl: int | None = None) -> None
    + def __init__(self, cache_service: CacheService, query_type: str, default_ttl: int | None = None) -> 
        # Initialize query repository.
    - def _make_query_key(self, query_params: dict[str, Any]) -> str
        # Create cache key from query parameters.
    + async def get_query_result(self, query_params: dict[str, Any], default_func: Callable[, T], ttl: int | None = None) -> T
        # Get query result from cache or execute query.
    + async def invalidate_query(self, query_params: dict[str, Any]) -> bool
        # Invalidate a specific query result.

+ class CollectionRepository:
    # RepositoryProtocol for caching collections/lists.
    __init__(self, cache_service: CacheService, collection_type: str, default_ttl: int | None = None) -> None
    + def __init__(self, cache_service: CacheService, collection_type: str, default_ttl: int | None = None) -> 
        # Initialize collection repository.
    - def _make_collection_key(self, filters: dict[str, Any] | None = None, pagination: dict[str, Any] | None = None, sort: dict[str, Any] | None = None) -> str
        # Create cache key from collection parameters.
    + async def get_collection(self, filters: dict[str, Any] | None = None, pagination: dict[str, Any] | None = None, sort: dict[str, Any] | None = None, default_func: Callable[, list[T]] | None = None, ttl: int | None = None) -> list[T] | None
        # Get collection from cache.
    + async def save_collection(self, collection: list[T], filters: dict[str, Any] | None = None, pagination: dict[str, Any] | None = None, sort: dict[str, Any] | None = None, ttl: int | None = None) -> bool
        # Save collection to cache.
    + async def invalidate_collections(self, filters: dict[str, Any] | None = None) -> None
        # Invalidate collections matching filters.

+ class ConfigurationRepository:
    # RepositoryProtocol for caching configuration data.
    __init__(self, cache_service: CacheService, config_type: str = 'app', default_ttl: int = 3600) -> None
    + def __init__(self, cache_service: CacheService, config_type: str = 'app', default_ttl: int = 3600) -> 
        # Initialize configuration repository.
    + async def get_config(self, config_key: str, environment: str | None = None, default_func: Callable[, dict[str, Any]] | None = None, ttl: int | None = None) -> dict[str, Any] | None
        # Get configuration by key.
    + async def set_config(self, config_key: str, config_data: dict[str, Any], environment: str | None = None, ttl: int | None = None) -> bool
        # Set configuration data.
    + async def get_config_value(self, config_key: str, value_key: str, environment: str | None = None, default: Any = None) -> Any
        # Get a specific configuration value.
    + async def invalidate_config(self, config_key: str, environment: str | None = None) -> bool
        # Invalidate configuration cache.

+ global T

+ global K

## semantic/__init__.py
  # Semantic cache for LLM response caching with vector similarity search.

- def __getattr__(name: str) -> Any

- def __dir__() -> Any

## semantic/cost_decision.py
  # Cost-aware semantic cache hit decision logic.

+ class CostAwareCacheDecision:
    # Cost-aware cache hit/miss decision function.
    __init__(self, accuracy_weight: float = 0.7) -> None
    + def __init__(self, accuracy_weight: float = 0.7) -> None
        # Initialize the cost-aware decision function.
    + def should_use_cache(self, similarity: float, api_cost_per_1k_tokens: float, expected_tokens: int) -> bool
        # Decide whether to use a cached response.

## semantic/protocols.py
  # Internal protocols for semantic cache vector indexing.

+ @runtime_checkable
+ class VectorIndexProtocol:
    # Internal protocol for vector similarity search backends.
    + @property
    + def size(self) -> int ...

## semantic/store.py
  # Three-tier semantic cache store for LLM response caching.

+ class SemanticCacheStore:
    # Three-tier semantic cache: exact hash → vector similarity → miss.
    __init__(self, cache_backend: CacheBackendProtocol, embedding_client: EmbeddingClientProtocol, vector_index: VectorIndexProtocol, similarity_threshold: float = 0.95, cache_ttl: int | None = None) -> None
    + def __init__(self, cache_backend: CacheBackendProtocol, embedding_client: EmbeddingClientProtocol, vector_index: VectorIndexProtocol, similarity_threshold: float = 0.95, cache_ttl: int | None = None) -> None
        # Initialize the semantic cache store.
    + async def lookup(self, query: str) -> str | None
        # Look up a query in the cache.
    + async def store(self, query: str, response: str, model: str) -> None
        # Store a query-response pair in both tiers.
    + async def invalidate(self, query: str) -> bool
        # Invalidate a cached entry by query.
    - @staticmethod
    - def _normalize_query(query: str) -> str
        # Normalize query by lowercasing and stripping whitespace.
    - @staticmethod
    - def _hash_query(query: str) -> str
        # Compute SHA256 hash of normalized query.

## semantic/vector_index.py
  # FAISS-backed vector index for semantic cache.

+ class FaissVectorIndex:
    # FAISS-backed in-memory vector index for semantic cache.
    __init__(self, embedding_dim: int = 384, max_entries: int = 100000) -> None
    + def __init__(self, embedding_dim: int = 384, max_entries: int = 100000) -> None
        # Initialize the FAISS vector index.
    + async def search(self, embedding: list[float], k: int = 1) -> list[tuple[str, float]]
        # Search for the top-k most similar embeddings.
    + async def add(self, key: str, embedding: list[float]) -> None
        # Add an embedding to the index.
    + async def remove(self, key: str) -> bool
        # Remove an entry from the index by cache key.
    + @property
    + def size(self) -> int
        # Number of entries currently indexed (excluding deleted entries).

## serialization/base.py
  # Serialization abstraction layer for Lexigram Cache.

+ class CacheSerializationError:
    # Raised when cache serialization or deserialization fails.
    __init__(self, message: str = 'Cache serialization failed', **kwargs) -> None
    + def __init__(self, message: str = 'Cache serialization failed', **kwargs) -> None
        # Initialize cache serialization error.

## serialization/compression.py
  # Cache serializer with automatic compression for large values.

+ class CompressingSerializer:
    # AsyncStringSerializerProtocol with automatic compression for large values.
    __init__(self, compression_threshold: int = const.DEFAULT_COMPRESSION_THRESHOLD, compression_level: int = const.DEFAULT_COMPRESSION_LEVEL) -> None
    + def __init__(self, compression_threshold: int = const.DEFAULT_COMPRESSION_THRESHOLD, compression_level: int = const.DEFAULT_COMPRESSION_LEVEL) -> None
        # Initialize serializer.
    + async def serialize(self, value: Any) -> str
        # Serialize and optionally compress value.
    + async def deserialize(self, value: str) -> Any
        # Deserialize and decompress if needed.
    + def get_stats(self) -> dict[str, Any]
        # Get serializer statistics.

## serialization/factory.py
  # AsyncStringSerializerProtocol helpers for provider initialization.

+ def create_serializers(pickle_hmac_key: str | None = None, allow_pickle: bool) -> dict[str, CacheSerializerProtocol]
    # Return available serializer instances keyed by name.

## serialization/json.py
  # JSON-based serializer implementation for Lexigram Cache.

+ class JSONSerializer:
    # High-performance JSON-based serializer with enhanced type support.
    + async def serialize(self, value: Any) -> str
        # Serialize a Python object to JSON string using orjson (5-10x faster).
    + async def deserialize(self, value: str) -> Any
        # Deserialize a JSON string back to a Python object.

## serialization/msgpack.py
  # MessagePack serializer for Lexigram Cache.

+ class MsgPackSerializer:
    # Binary MessagePack serializer for cache backends.
    __init__(self, use_bin_type: bool, raw: bool) -> None
    + def __init__(self, use_bin_type: bool, raw: bool) -> None
        # Initialise the serializer, verifying msgpack is importable.
    + async def serialize(self, value: Any) -> str
        # Serialize *value* to a Base64-encoded MessagePack string.
    + async def deserialize(self, value: str) -> Any
        # Deserialize a Base64-encoded MessagePack string back to a Python value.

## serialization/pickle.py
  # HMAC-signed pickle serializer for Lexigram Cache.

+ class PickleSerializer:
    # HMAC-SHA256-signed pickle serializer for Python object caching.
    __init__(self, hmac_key: bytes | str | list[bytes], protocol: int = pickle.HIGHEST_PROTOCOL) -> None
    + def __init__(self, hmac_key: bytes | str | list[bytes], protocol: int = pickle.HIGHEST_PROTOCOL) -> None
    + def rotate_key(self, new_key: bytes) -> None
        # Prepend *new_key* as the active signing key.
    - def _sign(self, data: bytes) -> str
        # Return the HMAC-SHA256 hex digest of *data* using the current key.
    - def _verify(self, sig: str, data: bytes) -> bool
        # Return ``True`` if *sig* matches *data* for any registered key.
    + async def serialize(self, value: Any) -> str
        # Pickle *value*, sign it, and return a ``<hmac>:<hex>`` string.
    + async def deserialize(self, value: str) -> Any
        # Verify the HMAC signature and unpickle the payload.

## service/core.py
  # Core cache service implementation for Lexigram Framework.

+ @inject
+ class CacheService:
    # High-level cache service with advanced features.
    __init__(self, provider: CacheProvider | None = None, config: CacheOperationConfig | None = None, protection: StampedeProtectedCache | None = None, backend: CacheBackendProtocol | None = None, ctx: Context | None = None, max_tags: int = 10000) -> None
    + def __init__(self, provider: CacheProvider | None = None, config: CacheOperationConfig | None = None, protection: StampedeProtectedCache | None = None, backend: CacheBackendProtocol | None = None, ctx: Context | None = None, max_tags: int = 10000) -> 
        # Initialize the cache service.
    - def _get_backend(self, name: str | None = None) -> CacheBackendProtocol
        # Resolve backend from direct injection or provider.
    + async def close(self) -> None
        # Close the cache service, releasing any background resources.
    - def _get_namespaced_key(self, key: str, request_scoped: bool = False) -> str
        # Get a namespaced key with optional request scoping.
    - def _add_ttl_jitter(self, ttl: int | None) -> int | None
        # Add jitter to TTL to prevent cache stampede.
    + async def get(self, key: str, backend: str | None = None, default: Any = None, request_scoped: bool = False) -> Any
        # Get a value from cache with error handling.
    + async def set(self, key: str, value: Any, ttl: int | None = None, backend: str | None = None) -> bool
        # Set a value in cache with error handling.
    + async def delete(self, key: str, backend: str | None = None) -> bool
        # Delete a value from cache.
    + async def delete_pattern(self, pattern: str, backend: str | None = None) -> int
        # Delete all keys matching a glob-style pattern.
    + async def exists(self, key: str, backend: str | None = None) -> bool
        # Check if a key exists in cache.
    + async def clear(self, backend: str | None = None) -> bool
        # Clear all values from cache.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Get comprehensive health status of the cache service.
    + def get_metrics(self) -> dict[str, int]
        # Get service performance metrics.
    + def reset_metrics(self) -> None
        # Reset performance metrics.
    + async def get_typed(self, key: str, type_: type[_T], backend: str | None = None, default: _T | None = None) -> _T | None
        # Get a value from cache and cast it to the requested type.

## service/decorators.py
  # Caching decorators for Lexigram Framework.

+ class CacheDecorator:
    # Advanced caching decorator with multiple strategies.
    __init__(self, service: CacheService, strategy: str = 'remember', key_prefix: str = '', ttl: int | None = None, backend: str | None = None, protect: bool = True, condition: Callable[, bool] | None = None) -> None
    + def __init__(self, service: CacheService, strategy: str = 'remember', key_prefix: str = '', ttl: int | None = None, backend: str | None = None, protect: bool = True, condition: Callable[, bool] | None = None) -> 
        # Initialize the cache decorator.
    + def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]
        # Apply the caching decorator.

+ def cache(service: CacheService, key_prefix: str = 'cache', ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Callable[, Callable[..., Any]]
    # Decorator to cache function results with custom key generation.

+ def remember(service: CacheService, ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Callable[, Callable[..., Any]]
    # Decorator to remember function results (memoization).

+ def conditional_cache(service: CacheService, condition_func: Callable[, bool], key_prefix: str = 'cond', ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Callable[, Callable[..., Any]]
    # Decorator to cache function results only when condition is met.

+ def invalidate_cache(service: CacheService, key_pattern: str, backend: str | None = None) -> Callable[, Callable[..., Any]]
    # Decorator to invalidate cache keys after function execution.

## service/factory.py
  # Service factory helpers for provider initialization.

+ def create_service(provider: Any, backend_name: str, backend: CacheBackendProtocol, protection: StampedeProtectedCache | None) -> CacheService
    # Create and return a CacheService instance for a backend.

## service/health.py
  # Health and metrics helpers for the Lexigram cache provider.

+ async def get_health_status(services: dict[str, CacheService], backends: dict[str, CacheBackendProtocol]) -> HealthCheckResult
    # Aggregate health across all cache services and backends.

+ async def get_metrics(services: dict[str, CacheService], backends: dict[str, CacheBackendProtocol], protection: StampedeProtectedCache | None) -> dict[str, Any]
    # Collect metrics from all registered cache services.

## service/invalidation.py
  # Tag-based and pattern invalidation mixin.

+ class InvalidationMixin:
    # Mixin providing tag-based cache invalidation for CacheService.
    + async def set_with_tags(self, key: str, value: Any, tags: list[str], ttl: int | None = None, backend: str | None = None) -> bool
        # Set a value in cache and associate it with one or more tags.
    + async def invalidate_by_tag(self, tag: str, backend: str | None = None) -> int
        # Delete all cache keys associated with *tag*.

## service/patterns.py
  # Cache-aside, write-through, and stampede-protected pattern mixin.

+ class PatternsMixin:
    # Mixin providing cache-aside and stampede-protected patterns for CacheService.
    + async def get_or_set(self, key: str, default_func: Callable[, Any], ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Any
        # Get a value from cache or compute and set it.
    + async def get_or_set_result(self, key: str, default_func: Callable[, Result[_T, _E] | Any], ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Result[_T, _E]
        # Get a value from cache or compute and set it, returning ``Result[T, E]``.
    + async def get_or_compute(self, key: str, factory: Callable[, Any], ttl: int | None = None, backend: str | None = None) -> Any
        # Get a value from cache or compute it with stampede protection.
    + async def remember(self, key: str | None = None, ttl: int | None = None, backend: str | None = None, protect: bool = True) -> Callable[, Callable[..., Any]]
        # Decorator to cache function results.

## service/pipeline.py
  # Batch/pipeline cache operations mixin.

+ class PipelineMixin:
    # Mixin providing batch/pipeline cache operations for CacheService.
    + async def get_many(self, keys: list[str], backend: str | None = None) -> dict[str, Any]
        # Get multiple values from cache.
    + async def set_many(self, items: dict[str, Any], ttl: int | None = None, backend: str | None = None) -> bool
        # Set multiple values in cache.
    + async def delete_many(self, keys: list[str], backend: str | None = None) -> bool
        # Delete multiple values from cache.

## service/registry.py
  # Cache status handler registry for metrics collection.

+ class HitStatusHandler:
    # Handler for HIT cache status.
    + def can_handle(self, status: CacheStatus) -> bool
    + async def record(self, metrics: CacheMetrics, count: int) -> None

+ class MissStatusHandler:
    # Handler for MISS cache status.
    + def can_handle(self, status: CacheStatus) -> bool
    + async def record(self, metrics: CacheMetrics, count: int) -> None

+ class SetStatusHandler:
    # Handler for SET cache status.
    + def can_handle(self, status: CacheStatus) -> bool
    + async def record(self, metrics: CacheMetrics, count: int) -> None

+ class DeleteStatusHandler:
    # Handler for DELETE cache status.
    + def can_handle(self, status: CacheStatus) -> bool
    + async def record(self, metrics: CacheMetrics, count: int) -> None

+ class ErrorStatusHandler:
    # Handler for ERROR cache status.
    + def can_handle(self, status: CacheStatus) -> bool
    + async def record(self, metrics: CacheMetrics, count: int) -> None

+ class CacheStatusRegistry:
    # Registry for cache status handlers.
    __init__(self) -> None
    + def __init__(self) -> None
        # Initialize the registry with default handlers.
    + def register(self, handler: CacheStatusHandler) -> None
        # Register a new status handler.
    + async def record(self, status: CacheStatus, metrics: CacheMetrics, count: int = 1) -> None
        # Record a cache status event.

+ def get_cache_status_registry() -> CacheStatusRegistry
    # Get the global cache status registry.

+ def reset_cache_status_registry() -> None
    # Reset the global cache status registry.

## service/request_cache.py
  # Request-scoped in-process cache backed by :mod:`contextvars`.

+ def get_request_cache() -> dict[str, Any]
    # Return the current request's cache dict, creating it if needed.

+ def clear_request_cache() -> None
    # Reset the current request's cache to an empty state.

+ def cache_in_request(func: _F) -> _F
    # Cache the result of an async function for the duration of the current request.

## service/stampede.py
  # Stampede protection utilities extracted from `protection.py`.

+ @inject
+ class StampedeProtectedCache:
    # Cache with stampede (thundering-herd) protection.
    __init__(self, cache: CacheBackendProtocol, lock_timeout: int, lock_wait_timeout: float) -> None
    + def __init__(self, cache: CacheBackendProtocol, lock_timeout: int, lock_wait_timeout: float) -> None
    + async def get_or_compute(self, key: str, compute: Callable[..., Any], ttl: int = 300, ttl_jitter: float, *args: Any, **kwargs: Any) -> Any
        # Get value from cache or compute it with stampede protection.
    - async def _get_from_cache(self, key: str) -> CacheEntry | None
        # Get cache entry via CacheBackendProtocol.
    - async def _compute_and_cache(self, key: str, compute: Callable[..., Any], ttl: int, *args: Any, **kwargs: Any) -> Any
        # Compute value and store in cache.
    + async def invalidate(self, key: str) -> bool
        # Invalidate a cache entry.
    - def _add_jitter(self, ttl: int, jitter_factor: float) -> int
        # Return TTL with optional random jitter applied.
    - async def _should_refresh_early(self, entry: CacheEntry, ttl: int) -> bool
        # Return True when probabilistic early refresh should be triggered.

## service/warmer.py
  # CacheWarmer — proactive cache pre-loading at boot or on schedule (D6.4).

+ class CacheWarmer:
    # Proactively fills cache entries from a loader function.
    __init__(self, cache: CacheBackendProtocol, concurrency: int = 10) -> None
    + def __init__(self, cache: CacheBackendProtocol, concurrency: int = 10) -> None
    + async def warm(self, keys: list[str], loader: Callable[, Awaitable[Any]], ttl: int | None = None, skip_existing: bool = True) -> dict[str, bool]
        # Pre-fill *keys* using *loader*.
    + async def warm_dict(self, data: dict[str, Any], ttl: int | None = None) -> int
        # Directly populate the cache from a pre-fetched dictionary.

## stores/redis_lock.py
  # Redis lock store implementation

+ class RedisLockStore:
    # Redis implementation of LockStore with owner validation.
    __init__(self, url: str = '', prefix: str = '', client: Any | None = None) -> None
    + def __init__(self, url: str = '', prefix: str = '', client: Any | None = None) -> 
    - async def _get_client(self) -> Any
        # Lazy client initialization
    - def _key(self, key: str) -> str
        # Apply prefix to key
    + async def acquire(self, resource: str, ttl: int = 30, owner: str = ...) -> str | None
        # Acquire a lock.
    + async def release(self, resource: str, lock_id: str) -> None
        # Release a lock only if `lock_id` matches the current owner.
    + async def extend(self, resource: str, lock_id: str, ttl: int) -> None
        # Extend TTL of a lock only if `lock_id` matches the current owner.
    + async def is_locked(self, key: str) -> bool
        # Check if a key is locked
    + @asynccontextmanager
    + async def locked(self, resource: str, ttl: int = 30, owner: str | None = None) -> Any
        # Async context manager that acquires a lock and releases it on exit.
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the lock store

## stores/redis_secrets.py
  # Redis secret store implementation.

+ class RedisSecretStore:
    # Redis implementation of SecretStore with optional at-rest encryption.
    __init__(self, url: str = '', prefix: str = '', encryption_key: bytes | str | None = None, client: Any | None = None) -> None
    + def __init__(self, url: str = '', prefix: str = '', encryption_key: bytes | str | None = None, client: Any | None = None) -> 
    - def _encrypt(self, value: str) -> str
        # Encrypt a plaintext value if encryption is configured.
    - def _decrypt(self, value: str) -> str
        # Decrypt a ciphertext value if encryption is configured.
    - async def _get_client(self) -> redis.Redis
        # Lazy client initialization
    - def _key(self, key: str) -> str
        # Apply prefix to key
    + async def get_secret(self, key: str) -> str | None
        # Get a secret by name, decrypting if encryption is configured.
    + async def set_secret(self, key: str, value: str) -> None
        # Set a secret, encrypting if encryption is configured.
    + async def delete_secret(self, key: str) -> None
        # Delete a secret
    + async def list_secrets(self, prefix: str | None = None) -> list[str]
        # List secrets with optional prefix
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the secret store

+ global redis: Any = None

+ global RedisError: type[Exception] = Exception

## stores/redis_state.py
  # Redis state store implementation

+ class RedisDriver:
    # Shared Redis connection logic
    __init__(self, url: str = '', prefix: str = '', client: Any | None = None) -> None
    + def __init__(self, url: str = '', prefix: str = '', client: Any | None = None) -> 
    - async def _get_client(self) -> Any
        # Lazy client initialization with connection health checks.
    - def _key(self, key: str) -> str
        # Apply prefix to key
    - def _json_encoder(self, obj: Any) -> Any
        # Enhanced JSON encoder for Python types.

+ class RedisStateStore:
    # Redis implementation of StateStoreProtocol
    + async def get(self, key: str) -> Any | None
        # Get a value by key
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> None
        # Set a value with optional TTL
    + async def delete(self, key: str) -> bool
        # Delete a value by key
    + async def get_bulk(self, keys: list[str]) -> dict[str, Any]
        # Get multiple values by keys
    + async def health_check(self, timeout: float = 5.0) -> HealthCheckResult
        # Check the health of the state store

+ global RedisError: type[Exception] = Exception

## strategies/tiered.py
  # Tiered caching strategy for Lexigram Cache.

+ class TieredCache:
    # Tiered caching matching (L1 -> L2).
    __init__(self, cache_service: CacheService, l1_backend: str = 'memory', l2_backend: str = 'redis', l1_ttl_multiplier: float = 0.5) -> None
    + def __init__(self, cache_service: CacheService, l1_backend: str = 'memory', l2_backend: str = 'redis', l1_ttl_multiplier: float = 0.5) -> 
        # Initialize tiered cache.
    + async def get(self, key: str, default: Any = None) -> T | None
        # Get value from tiered cache.
    + async def set(self, key: str, value: Any, ttl: int | None = None) -> bool
        # Set value in both L1 and L2.
    + async def delete(self, key: str) -> bool
        # Delete from both tiers.
    + async def shutdown(self) -> None
        # Shut down the tiered cache in L1 → L2 order.
    + async def get_or_set(self, key: str, default_func: Callable[, Any], ttl: int | None = None) -> T
        # Tiered get-aside pattern.

+ global T

## strategies/write_through.py
  # Write-through caching strategy for Lexigram Cache.

+ class WriteThroughCache:
    # Write-through caching strategy.
    __init__(self, cache_service: CacheService, namespace: str, ttl: int | None = None, key_field: str = 'id') -> None
    + def __init__(self, cache_service: CacheService, namespace: str, ttl: int | None = None, key_field: str = 'id') -> 
    - def _make_key(self, entity_id: Any) -> str
    + async def get(self, entity_id: Any, loader: Callable[, Any]) -> T
        # Get from cache, or load and fill cache (Read-through)
    + async def update(self, entity_id: Any, data: T, writer: Callable[, Any]) -> T
        # Update cache after writing to primary store (Write-through)
    + async def delete(self, entity_id: Any, deleter: Callable[, Any]) -> bool
        # Remove from cache after removing from primary store
    + async def shutdown(self) -> None
        # Flush any pending state and release resources.

+ def write_through(cache_service: CacheService, namespace: str, ttl: int | None = None, key_field: str = 'id') -> 
    # Decorator for repository methods to implement write-through caching.

+ global T

## types.py
  # Core type definitions for lexigram-cache.

+ class BackendType:
    # Supported cache backend types.
    MEMORY = 'memory'
    REDIS = 'redis'
    MEMCACHED = 'memcached'

+ class CacheStatus:
    # Status values for cache operations.
    HIT = 'hit'
    MISS = 'miss'
    SET = 'set'
    DELETE = 'delete'
    ERROR = 'error'
    EXPIRED = 'expired'
    STALE = 'stale'

+ @dataclass
+ class CacheItem:
    # Represents a cached item with metadata.
    key: str
    value: Any
    ttl: int | None = None
    created_at: datetime
    accessed_at: datetime | None = None
    access_count: int = 0
    tags: list[str]
    version: str | None = None

+ @dataclass
+ class CacheResult:
    # Result of a cache operation.
    status: CacheStatus
    value: T | None = None
    key: str | None = None
    latency_ms: float | None = None
    from_backend: str | None = None
    metadata: dict[str, Any]

+ @dataclass
+ class CacheMetrics:
    # Cache performance metrics with atomic updates.
    hits: int = 0
    misses: int = 0
    sets: int = 0
    deletes: int = 0
    errors: int = 0
    total_latency_ms: float = 0.0
    operation_count: int = 0
    _lock: asyncio.Lock

+ @dataclass
+ class CacheStats:
    total_keys: int = 0
    memory_usage_bytes: int = 0
    backends: dict[str, dict[str, Any]]
    metrics: CacheMetrics | None = None
    health_status: HealthStatus

+ @dataclass
+ class CacheHealthResult:
    status: HealthStatus
    message: str = ''
    latency_ms: float = 0.0
    backends: dict[str, dict[str, Any]]
    details: dict[str, Any]

+ @dataclass
+ class TaggedCacheKey:
    key: str
    tags: list[str]

+ @dataclass
+ class DistributedLockInfo:
    # Lock ownership information for distributed locks.
    key: str
    owner: str
    acquired_at: datetime
    ttl: int
    renewal_task: asyncio.Task | None = None

+ @dataclass
+ class CacheEntry:
    # Cache entry with metadata for stampede protection.
    value: T
    cached_at: datetime
    expires_at: datetime

+ class CacheStatusHandler:
    # Protocol for cache status handlers.
    + def can_handle(self, status: CacheStatus) -> bool ...

+ global T