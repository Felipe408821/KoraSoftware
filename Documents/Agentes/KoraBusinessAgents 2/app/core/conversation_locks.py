import asyncio
from collections import defaultdict


_locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)


def get_phone_lock(phone: str) -> asyncio.Lock:
    return _locks[phone]
