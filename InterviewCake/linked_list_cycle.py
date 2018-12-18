'''
Created on Dec 17, 2018

@author: USOMZIA
'''
import unittest
from win32com.test.testall import verbosity
def contains_cycle(first_node):
    node_already_seen = set()
    current_node = first_node
        
    while current_node.next:
        if current_node in node_already_seen:
            return True
        else:
            node_already_seen.add(current_node)
            
        current_node = current_node.next
            
    return False

def contains_cycle_less_space(first_node):
    fast_pointer = first_node
    slow_pointer = first_node
        
    while fast_pointer != None and fast_pointer.next != None:
        if fast_pointer.next == slow_pointer:
            return True
        else:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
    return False


class Test(unittest.TestCase):
    class LinkedListNode(object):
        def __init__(self, value, next = None):
            self.value = value
            self.next = next
    def test_linked_list_with_no_cycle(self):
        fourth = self.LinkedListNode(4)
        third = self.LinkedListNode(3, fourth)
        second = self.LinkedListNode(2, third)
        first = self.LinkedListNode(1, second)
        result = contains_cycle_less_space(first)
        self.assertFalse(result)
        
    def test_two_node_cycle_at_end(self):
        fifth = self.LinkedListNode(5)
        fourth = self.LinkedListNode(4, fifth)
        third = self.LinkedListNode(3, fourth)
        second = self.LinkedListNode(2, third)
        first = self.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)
        
    def test_cycle_loops_to_middle(self):
        fifth = self.LinkedListNode(5)
        fourth = self.LinkedListNode(4, fifth)
        third = self.LinkedListNode(3, fourth)
        second = self.LinkedListNode(2, third)
        first = self.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle_less_space(first)
        self.assertTrue(result)
        
        
        
unittest.main(verbosity = 2)

        
    
    
    
        
            