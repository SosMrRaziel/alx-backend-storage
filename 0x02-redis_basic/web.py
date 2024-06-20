#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


# Initialize a Redis store
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Decorator to cache the output of a method."""
    @wraps(method)
    def invoker(url) -> str:
        """Invokes the method and caches the result."""
        # Increment the count for the given URL
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            # If the result is cached, return it
            return result.decode('utf-8')
        # Otherwise, compute the result using the method
        result = method(url)
        # Reset the count for the URL
        redis_store.set(f'count:{url}', 0)
        # Cache the result for 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Returns the content of a web page."""
    return requests.get(url).text
