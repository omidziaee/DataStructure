'''
Created on Jul 2, 2018

@author: USOMZIA
'''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
s = Stack()
print s.isEmpty()
s.push(1)
s.push('two')
print s.peek()
s.pop()
print s.peek() 
print s.isEmpty()
s.pop()
print s.isEmpty() 