#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in Redis """
import redis
import uuid
from typing import Union, Callable
import functools


class Cache:
    def __init__(self):
        """
        Initializes the Cache class.
        Creates a private variable _redis with an instance of the Redis client.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush the Redis database

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key.
        Returns the generated key.
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis
        return key

    @functools.wraps(store)
    def store_counted(self, data: Union[str, bytes, int, float]) -> str:
        """
        Decorated version of the store method that increments the call count.
        """
        key = self.store(data)  # Call the original store method
        self._increment_call_count(self.store_counted.__qualname__)  # Increment call count
        return key

    def _increment_call_count(self, method_name: str) -> None:
        """
        Increments the call count for the specified method.
        """
        count_key = f"call_count:{method_name}"
        self._redis.incr(count_key)

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis based on the provided key.
        Optionally applies the conversion function (fn) to the retrieved data.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """Convenience method to retrieve data as a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Convenience method to retrieve data as an integer."""
        return self.get(key, fn=int)