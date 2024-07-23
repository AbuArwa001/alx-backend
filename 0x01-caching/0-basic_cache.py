#!/usr/bin/python3
""" Basic Caching """
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """BasicCaching class Containing two methods"""
    def __init__(self):
        super().__init__()
    def put(self, key, item):
        """Set cache data"""
        if key and item:
            self.cache_data.update({key: item})
    def get(self, key):
        """Get cache data"""
        return self.cache_data.get(key, None)