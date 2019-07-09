'''
Created on Jul 6, 2019

@author: omid

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
# we need to have a doubly linked list as in array if we delete or shift the elements we need to shift it
# right or left
class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache(object):    
    def __init__(self, capacity):
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity
        # These are tow dummy nodes in order to prevent handling the null at the end or front
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key):
        if key in self.map:
            # we should remove it from the list and add it either to end or front
            n = self.map[key]
            self._remove(n)
            self._add(n)
            return self.map[key].val
        return -1
    # for inner functions it is better to add _ in front of it then with tab it does not being shown
    def _remove(self, node):
        # we need to ignore the links of the current node
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    def _add(self, node):
        # we are going to add it to the end of the list
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p 
        node.next = self.tail
    def put(self, key, value):
        # Check if it already exists we need to update value but we need to bring it either to the end or front
        node = Node(key, value)
        if key in self.map:
            # It is important to get it from dic and remove it you can not do self._remove(node)
            # because the prev and next of the new created node is unknown
            self._remove(self.map[key])
        self.map[key] = node
        self._add(node)
        if len(self.map) > self.capacity:
            rem_node = self.head.next
            key = rem_node.key
            # remove the least used from both map and list
            del self.map[key]
            self._remove(rem_node)
        
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
print obj.get(2)
obj.put(1, 1)
obj.put(4, 1)
print obj.get(2)