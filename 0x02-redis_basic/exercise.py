#!/usr/bin/env python3
"""
A python class
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count how many times methods of the
    Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        decorated function and return the wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrap the decorated function and return the wrapper
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


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

    @call_history
    @count_calls
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
