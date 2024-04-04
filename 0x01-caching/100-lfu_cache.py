#!/usr/bin/python3
""" Contains MRU class """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching implementation """

    def __init__(self):
        """ Initialization """
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """ assigns key & item to cache_data """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    k = min(self.keys, key=self.keys.get)
                    self.cache_data.pop(k)
                    print(f'DISCARD: {k}')
                    self.keys.pop(k)
                if key not in self.keys:
                    self.keys[key] = 0

    def get(self, key):
        """ Retrieves item from cache """
        value = self.cache_data.get(key, None)
        if value:
            self.keys[key] += 1
        return value
