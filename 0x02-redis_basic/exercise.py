#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in Redis """
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[
                str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key.
        Optionally applies the conversion function `fn` to the retrieved data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis as a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis as an integer.
        """
        return self.get(key, fn=int)
