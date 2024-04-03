#!/usr/bin/python3
""" Contains LIFOCache class """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implementation """
    def __init__(self):
        """ Instantiation """
        super().__init__()
        self.last_item = None

    def put(self, key, item):
        """ assigns key & item to cache_data """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.last_item)
                    print(f'DISCARD: {self.last_item}')
                self.last_item = key

    def get(self, key):
        """ returns the/a value in cache_data[key] """
        if not key:
            return None
        else:
            return self.cache_data.get(key)
