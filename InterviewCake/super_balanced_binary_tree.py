'''
Created on Dec 19, 2018

@author: USOMZIA
'''
import unittest


def is_balanced(tree_node):
    # the min and max depth of the leaves should not exceed one
    # This is a stack to keep the nodes and their depths
    # each element is a tuple indicating the node and its depth
    if not tree_node.left and not tree_node.right:
        return True
    stack_keep_node_depth = []
    stack_keep_node_depth.append((tree_node, 0)) 
    max_depth = -float('inf')
    min_depth = float('inf')
    while stack_keep_node_depth:
        node, depth = stack_keep_node_depth.pop()
        if not node.left and not node.right:
            # We arrive to a new leaf
            max_depth = max(max_depth, depth)
            min_depth = min(min_depth, depth)
            if min_depth > 0 and max_depth > 0:
                if max_depth - min_depth > 1:
                    return False
        else:
            if node.right:
                stack_keep_node_depth.append((node.right, depth + 1))
            if node.left:
                stack_keep_node_depth.append((node.left, depth + 1))
    return True
    
    
def is_balanced_original(tree_node):
    # We need to traverse the binary tree and compare the depth of each leaf pair
    # This is not good because the worst case if the tree is prefect we need to do no_of_leaves ^ 2 comparison
    # No of all the Nodes exclude the last level + 1 = No of the Nodes in the last level
    # Therefore in worst case we need to compare o((n/2)^2) which is simply o(n^2) comparison
    # This is not good!
    # Instead of doing this we need to check the max(leaf_decpth) and min(leaf_depth)
    # Edge cases
    if (not tree_node):
        return True
    # Stack to traverse the tree
    node_depth = []
    node_depth.append((tree_node, 0))
    
    # We also need a data structure to keep the depths as we hit the end of each 
    # branch
    
    depths = []
    
    while len(node_depth) > 0:
        node, depth = node_depth.pop()
        
        # Now check if we arrive to a leaf node
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)
            # Now either if the length of depths is greater than 2 or 
            # max(depth) - min(depth) > 1 we need to return False
        if (len(depths) > 2) or (len(depths) == 2 and (abs(depths[1] - depths[0]) > 1)):
            return False
            # If it passses the top conditions now it is time to step forward
            # on the tree!
        if node.left:
            node_depth.append((node.left, depth + 1))
        if node.right:
            node_depth.append((node.right, depth + 1))
    return True

    
        


















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


    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)



unittest.main(verbosity=2)
        
        
        



    