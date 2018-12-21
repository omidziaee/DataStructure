'''
Created on Dec 20, 2018

@author: USOMZIA
'''
import unittest

def find_the_largest(root_node):
    # The largest node value is the most right side of the tree
    # We need a stack to keep the values in order to traverse the tree
    nodes = []
    nodes.append(root_node)
    
    while len(nodes) > 0:
        node = nodes.pop()
        # just push the right side nodes disregard the left side nodes
        if node.right:
            nodes.append(node.right)
    return node.value

def find_the_largest_recursive(root_node):
    # Base case
    if not root_node.right:
        return root_node.value
    max_node = find_the_largest_recursive(root_node.right)
    return max_node

class Test(unittest.TestCase):
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            
        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left
        
        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right
        
    def test_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        actual = find_the_largest_recursive(tree)
        expected = 80
        self.assertEqual(actual, expected)
        
    def test_ascending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(60)
        right_right = right.insert_right(70)
        right_right.insert_right(80)
        actual = find_the_largest_recursive(tree)
        expected = 80
        self.assertEqual(actual, expected)
        
unittest.main(verbosity = 2)
        