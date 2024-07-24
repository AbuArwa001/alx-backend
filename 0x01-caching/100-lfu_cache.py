#!/usr/bin/python3
"""FIFOCache  Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class Containing two methods"""
    def __init__(self):
        """LFUCache  class __init__ method"""
        super().__init__()
        self.freq_dict = {}
        self.discard = '0'

    def put(self, key, item):
        """Set cache data with proper caching algorithm."""
        lst = list(self.cache_data)
        ln = len(lst) + 1

        if key and item:
            if ln > BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    update = self.freq_dict.get(key, None)
                    if update and update > 0:
                        update += 1
                        self.freq_dict.update({key: update})
                        self.cache_data.update({key: item})
                else:
                    self.discard = min(self.freq_dict, key=self.freq_dict.get)
                    self.freq_dict.pop(self.discard)
                    self.freq_dict.update({key: 1})
                    self.cache_data.pop(self.discard)
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {self.discard}")
            else:
                self.freq_dict.update({key: 1})
                self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        update = self.freq_dict.get(key, None)
        if update and update > 0:
            update += 1
            self.freq_dict.update({key: update})
        return self.cache_data.get(key, None)
