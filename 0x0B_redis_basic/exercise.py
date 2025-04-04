#!/usr/bin/env python3
"""
cache module using redis to store data
"""

import redis
import uuid
from typing import Union


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
