#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in Redis """
import redis
import uuid
from typing import Union


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
