#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import Cache

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
