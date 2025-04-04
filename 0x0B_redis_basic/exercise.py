#!/usr/bin/env python3
"""
cache module using redis to store data
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """cache class for storing data in redis"""

    def __init__(self) -> None:
        """initialize redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redis under a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str, bytes, int, float, None
    ]:
        """retrieve value from redis and optionally apply a conversion"""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """get value and convert to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """get value and convert to int"""
        return self.get(key, fn=int)
