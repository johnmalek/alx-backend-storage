#!/usr/bin/env python3
"""
A python class
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        __init__ class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string
        """
        random_uuid = str(uuid.uuid4())
        self._redis.set(random_uuid, data)
        return random_uui

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, bytes, int, float]:
        """
        A method with Callable that will be
        used to convert data back to correct format
        """
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get
        with the correct conversion function
        """
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get
        with the correct conversion function
        """
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
