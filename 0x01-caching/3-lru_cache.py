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
        """Set cache data"""
        lst = list(self.cache_data)
        ln = len(lst) + 1

        if key and item:
            if ln > BaseCaching.MAX_ITEMS:
                for age, ky in enumerate(self.cache_data):
                    if key == ky:
                        continue
                    update = self.age_bits.get(ky, None)
                    # print(f"age: {age}")
                    if update and update > 0:
                        update -= 1
                        self.age_bits.update({ky: update})
                    elif update == 0 and key not in self.age_bits:
                        self.discard = ky
                        self.age_bits.pop(self.discard)

                # del self.cache_data[self.discard]
                if key not in self.age_bits:
                    self.cache_data.pop(self.discard)
                    print(f"DISCARD: {self.discard}")
            if key not in self.age_bits:
                self.age_bits.update({key: len(self.cache_data)})
            else:
                self.age_bits.update({key: 3})
            self.cache_data.update({key: item})

    def get(self, key):
        """Get cache data"""
        return self.cache_data.get(key, None)
