---
title: "lexigram-storage"
description: "Blob storage — S3, GCS, Azure, R2, and local filesystem drivers with presigned URLs and streaming."
sidebar:
  badge:
    text: Alpha
    variant: caution
---

:::note[Maturity]
Alpha (0.1.x). Public API may change before 1.0.
:::

Unified blob/object storage abstraction with drivers for S3, GCS, Azure Blob, Cloudflare R2, and local filesystem. Supports presigned URLs, streaming uploads/downloads, and content-type metadata.

## Installation

```bash
pip install lexigram-storage[aws]
```

Extras: `[aws]`, `[gcp]`, `[azure]`.

## Quick Start

```python
from lexigram.storage import StorageModule, StorageConfig, S3Driver

@module(imports=[
    StorageModule.configure(StorageConfig(driver=S3Driver, bucket="my-bucket"))
])
class AppModule(Module):
    pass
```

## Key Features

- `BlobStoreProtocol` abstraction with swappable drivers
- S3, GCS, Azure, and local/Memory drivers for dev
- Presigned URL generation for secure direct access
- Streaming upload and download
- KV storage for small string-keyed records with TTL
- Upload options with content-type and metadata

## Configuration

`StorageConfig` manages driver selection, bucket/container name, credentials, endpoint URL, and region.

## Related

- [Guide](/guides/storage/)
- [`lexigram-cache`](/ecosystem/lexigram-cache/) — caching layer
