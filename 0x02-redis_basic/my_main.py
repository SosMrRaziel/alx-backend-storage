#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import Cache
from typing import Union, Callable

if __name__ == "__main__":
    cache = Cache()
    data = 50
    key = cache.store(data)
    print(f"Stored key: {key}")

    retrieved_data = cache.get(key)
    print(f"Retrieved data (raw): {retrieved_data}")

    retrieved_str = cache.get_str(key)
    print(f"Retrieved data (str): {retrieved_str}")

    retrieved_int = cache.get_int(key)
    print(f"Retrieved data (int): {retrieved_int}")

    @cache.count_calls
    def custom_store(self, data: Union[str, bytes, int, float]) -> str:
        return self.store(data)

    custom_store(b"first")
    print(cache.get(custom_store.__qualname__))

    custom_store(b"second")
    custom_store(b"third")
    print(cache.get(custom_store.__qualname__))