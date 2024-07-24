#!/usr/bin/python3
"""FIFOCache  Caching """
BaseCaching = __import__('base_caching').BaseCaching


def most_recent(key, age_bits, cache_data):
    """Update age bits for access"""
    for _, ky in enumerate(cache_data):
        if key == ky:
            age_bits.update({key: 3})
            continue
        update = age_bits.get(ky, None)
        if update and update >= 2:
            update -= 1
            age_bits.update({ky: update})
    return age_bits


class LRUCache(BaseCaching):
    """LRUCache class Containing two methods"""
    def __init__(self):
        """LRUCache  class __init__ method"""
        super().__init__()
        self.age_bits = {}
        self.discard = '0'

    def put(self, key, item):
        """Set cache data with proper caching algorithm."""
        lst = list(self.cache_data)
        ln = len(lst) + 1

        if key and item:
            if ln > BaseCaching.MAX_ITEMS:
                for _, ky in enumerate(self.cache_data):
                    if key == ky:
                        continue
                    update = self.age_bits.get(ky, None)
                    if update and update > 0:
                        update -= 1
                        self.age_bits.update({ky: update})
                    elif update == 0 and key not in self.age_bits:
                        self.discard = ky
                        self.age_bits.pop(self.discard)
                if key not in self.age_bits:
                    self.cache_data.pop(self.discard)
                    print(f"DISCARD: {self.discard}")
            if key not in self.age_bits:
                self.age_bits.update({key: len(self.cache_data)})
            else:
                self.age_bits.update({key: 3})
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.age_bits = most_recent(key, self.age_bits, self.cache_data)
        return self.cache_data[key]
