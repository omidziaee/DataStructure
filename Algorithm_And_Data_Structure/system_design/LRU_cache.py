'''
Created on Jul 3, 2019

@author: USOMZIA
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.LRU = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) >= self.capacity:
            del self.cache[self.LRU[-1]]
        else:
            self.cache[key] = value
            self.LRU.append(LRU)
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print obj.get(1)
obj.put(3, 3)
print obj.get(2)





