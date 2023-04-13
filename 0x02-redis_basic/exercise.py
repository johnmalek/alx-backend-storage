#!/usr/bin/env python3
"""
A python class
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """"
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
       return random_uuid
