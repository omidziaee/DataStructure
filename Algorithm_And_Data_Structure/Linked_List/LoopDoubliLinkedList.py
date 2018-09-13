'''
Created on Aug 30, 2018

@author: USOMZIA
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
def listTraverse(head):
        current = head
        next = current.next
        while current != None:
            print current.value            
            current = current.next
            
def reverse(head):
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
b.previous = a
c.previous = b

listTraverse(c)