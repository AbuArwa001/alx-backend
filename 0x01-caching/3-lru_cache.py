#!/usr/bin/python3
"""LRU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


def most_recent(key, age_bits, cache_data):
    """Update age bits for access"""
    for _, ky in enumerate(cache_data):
        if key == ky:
            age_bits.update({key: 3})
            continue
        update = age_bits.get(ky, None)
        if update is not None and update >= 2:
            update -= 1
            age_bits.update({ky: update})
    return age_bits


class LRUCache(BaseCaching):
    """LRUCache class that inherits
    from BaseCaching and implements LRU caching"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.age_bits = {}
        self.discard = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.age_bits = most_recent(key, self.age_bits, self.cache_data)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least recently used item to discard
                self.discard = min(self.age_bits, key=self.age_bits.get)
                print(f"DISCARD: {self.discard}")
                del self.cache_data[self.discard]
                del self.age_bits[self.discard]

            self.age_bits[key] = 3  # Set age bit for the new item

        self.cache_data[key] = item
        self.age_bits = most_recent(key, self.age_bits, self.cache_data)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.age_bits = most_recent(key, self.age_bits, self.cache_data)
        return self.cache_data.get(key)
