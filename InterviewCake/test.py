import unittest


def find_second_largest(root_node):

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

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        actual = find_second_largest(tree)
        expected = 40
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)