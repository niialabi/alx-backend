#!/usr/bin/python3
""" Contains LIFOCache class """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ A LRU CACHEING IMPLEMENTATION """

    def __init__(self):
        """ Initialization """
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        """ ssigns key & item to cache_data  """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if key not in self.keys_list:
                    self.keys_list.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys_list[0])
                    print(f'DISCARD: {self.keys_list[0]}')
                    self.keys_list.pop(0)

    def get(self, key):
        """Retrieves an item from the cache."""
        item = self.cache_data.get(key, None)
        if item:
            self.keys_list.remove(key)
            self.keys_list.append(key)
        return item
