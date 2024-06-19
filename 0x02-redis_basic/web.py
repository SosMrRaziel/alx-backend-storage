#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in Redis """
import requests
import redis
import time
from functools import wraps

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(url):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if URL is already cached
            cached_content = r.get(f"content:{url}")
            if cached_content:
                print(f"Using cached content for {url}")
                return cached_content.decode('utf-8')

            # Fetch content from the URL
            response = requests.get(url)
            content = response.text

            # Cache the content with expiration time
            r.setex(f"content:{url}", 10, content)

            return content
        return wrapper
    return decorator

@cache_page("http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com")
def get_page(url: str) -> str:
    return requests.get(url).text
