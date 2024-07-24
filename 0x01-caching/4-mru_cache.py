#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache  class that inherits from
    BaseCaching and implements LRU caching"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move the existing key to the end to mark it as most recently used
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Cache is full, remove the least recently used item
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
