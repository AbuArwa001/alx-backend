#!/usr/bin/python3
"""FIFOCache  Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class Containing two methods"""
    def __init__(self):
        """LRUCache  class __init__ method"""
        super().__init__()
        self.age_bits = {}
        self.discard = '0'

    def put(self, key, item):
        """Set cache data with proper caching algorithm."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.age_bits[key] = BaseCaching.MAX_ITEMS - 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the key to discard
                discard_key = min(self.age_bits, key=self.age_bits.get)
                self.cache_data.pop(discard_key)
                self.age_bits.pop(discard_key)
                print(f"DISCARD: {discard_key}")

            self.cache_data[key] = item
            self.age_bits[key] = BaseCaching.MAX_ITEMS - 1

        # Update age bits for all other keys
        for k in list(self.age_bits):
            if k != key:
                self.age_bits[k] -= 1

    def get(self, key):
        """Get cache data"""
        return self.cache_data.get(key, None)
