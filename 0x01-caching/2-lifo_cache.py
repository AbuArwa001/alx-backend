#!/usr/bin/python3
"""FIFOCache  Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class Containing two methods"""
    def __init__(self):
        """LIFOCache  class __init__ method"""
        super().__init__()

    def put(self, key, item):
        """Set cache data"""
        lst = list(self.cache_data)
        ln = len(lst) + 1
        if key and item:
            if ln > BaseCaching.MAX_ITEMS:
                discard = lst[-1]
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")
            self.cache_data.update({key: item})

    def get(self, key):
        """Get cache data"""
        return self.cache_data.get(key, None)
