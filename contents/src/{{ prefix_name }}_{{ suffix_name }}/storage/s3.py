from __future__ import annotations

import aiobotocore.session

_client = None


async def init_s3(settings) -> None:
    global _client
    session = aiobotocore.session.get_session()
    kwargs = {
        "service_name": "s3",
        "aws_access_key_id": settings.s3_access_key,
        "aws_secret_access_key": settings.s3_secret_key,
        "region_name": "us-east-1",
    }
    if settings.s3_endpoint:
        kwargs["endpoint_url"] = settings.s3_endpoint
    _client = await session.create_client(**kwargs).__aenter__()


async def close_s3() -> None:
    global _client
    if _client is not None:
        await _client.__aexit__(None, None, None)
        _client = None


def get_s3():
    if _client is None:
        raise RuntimeError("S3 not initialized — call init_s3() first")
    return _client
