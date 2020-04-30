#https://www.interviewbit.com/problems/lru-cache/#
from collections import OrderedDict
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return self.cache[key]
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
        self.cache[key] = value
        if self.capacity<len(self.cache):
            self.cache.popitem(last = False)
            
        
        
