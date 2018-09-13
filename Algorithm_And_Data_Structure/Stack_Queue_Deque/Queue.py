'''
Created on Jul 2, 2018

@author: USOMZIA
'''
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    
q = Queue()
print q.isEmpty()
print q.size()
q.enqueue(5)
q.enqueue(6)
q.enqueue('two')
print q.dequeue()

                
        