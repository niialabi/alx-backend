#!/usr/bin/python3
""" Contains MRU class """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching system that inherits from BaseCaching."""

    def __init__(self):
        """ Initialization """
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        """ assigns key & item to cache_data """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys_list[-1])
                    print(f'DISCARD: {self.keys_list[-1]}')
                    self.keys_list.pop(-1)
                if key not in self.keys_list:
                    self.keys_list.append(key)

    def get(self, key):
        """Retrieves an item from the cache."""
        item = self.cache_data.get(key, None)
        if item:
            self.keys_list.remove(key)
            self.keys_list.append(key)
        return item
