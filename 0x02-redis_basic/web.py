#!/usr/bin/env python3
"""
python function
"""
import requests
import redis
from functools import wraps

st = redis.Redis()


def url_access(method):
    """
    decorator to track how many times a
    particular URL was accessed in the key 'count:{url}'
    """
    @wraps(method)
    def wrapper(url):
        """
        decorate the function and return the wrapper
        """
        cached_key = "cached:" + url
        cached_data = st.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        st.incr(count_key)
        st.set(cached_key, html)
        st.expire(cached_key, 10)
        return html
    return wrapper


@url_access
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a url and return it
    """
    response = requests.get(url)
    return response.text
