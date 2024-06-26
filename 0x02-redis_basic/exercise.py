#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


# Decorator to count the number of times a method is called
def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)  # Increment the counter in Redis
        return method(self, *args, **kwargs)

    return wrapper

# Decorator to store the history of inputs and outputs for a function
def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input) # Store input
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper

# Function to display the history of calls for a specific function
def replay(fn: Callable):
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    print("{} was called {} times:".format(function_name, value))
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        print("{}(*{}) -> {}".format(function_name, input, output))

# Cache class
class Cache:
    def __init__(self):
        self._redis = redis.Redis()  # Initialize Redis client
        self._redis.flushdb()  # Clear the database

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())  # Generate a random key (UUID)
        self._redis.set(random_key, data)  # Associate data with the key
        return random_key

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)  # Retrieve data from Redis
        if fn:
            value = fn(value)  # Apply conversion function if provided
        return value

    def get_str(self, key: str) -> str:
        value = self._redis.get(key)
        return value.decode("utf-8")  # Convert to string

    def get_int(self, key: str) -> int:
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))  # Convert to integer
        except Exception:
            value = 0
        return value
