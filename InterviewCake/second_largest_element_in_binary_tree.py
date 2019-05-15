'''
Created on Dec 20, 2018

@author: USOMZIA
'''

import unittest
def find_second_largest_with_stack(root_node):

    # Find the second largest item in the binary search tree
    if (not root_node.left and not root_node.right) or (not root_node):
        raise ValueError("Binary tree at least should have two values to find the second largest!")
    # this is the stack to traverse the tree
    keep_node_values = [(root_node, root_node.value)]
    while keep_node_values:
        node, value = keep_node_values.pop()
        if node.right and (not node.right.right and not node.right.left):
            return value
        if not node.right and node.left:
            return find_largest(node.left)
        if node.right and node.left:
            keep_node_values.append((node.right, node.right.value))
            
def find_largest(root_node):
    # Edge case
    if (not root_node):
        raise indexError("Binary Tree should at least have one value")
    stack_keep_value_node = [(root_node, root_node.value)]
    while stack_keep_value_node:
        node, value = stack_keep_value_node.pop()
        # Just check if the node has a right node
        if node.right:
            stack_keep_value_node.append((node.right, node.right.value))
        else:
            return value
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

def find_second_largest(root_node):
    if (not root_node) or (not root_node.right and not root_node.left):
        raise indexError("In order to find the second largest it should at least have two nodes!")
    current_node = root_node
    while current_node:
        if current_node.right and (not current_node.right.right and not current_node.right.left):
            return current_node.value
        if not current_node.right and current_node.left:
            return find_the_largest(current_node.left)
        current_node = current_node.right

def find_the_largest_recursive(root_node):
    # Base case
    if not root_node.right:
        return root_node.value
    max_node = find_the_largest_recursive(root_node.right)
    return max_node
    
    


















# Tests

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
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_child(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        actual = find_second_largest(tree)
        expected = 60
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_subtree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right_left = right.insert_left(60)
        right_left_left = right_left.insert_left(55)
        right_left.insert_right(65)
        right_left_left.insert_right(58)
        actual = find_second_largest(tree)
        expected = 65
        self.assertEqual(actual, expected)

    def test_second_largest_is_root_node(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        actual = find_second_largest(tree)
        expected = 50
        self.assertEqual(actual, expected)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        actual = find_second_largest(tree)
        expected = 40
        self.assertEqual(actual, expected)

    def test_ascending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(60)
        right_right = right.insert_right(70)
        right_right.insert_right(80)
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_error_when_tree_has_one_node(self):
        tree = Test.BinaryTreeNode(50)
        with self.assertRaises(Exception):
           find_second_largest(tree)

    def test_error_when_tree_is_empty(self):
        with self.assertRaises(Exception):
           find_second_largest(None)


unittest.main(verbosity=2)


