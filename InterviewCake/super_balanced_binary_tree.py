'''
Created on Dec 19, 2018

@author: USOMZIA
'''
import unittest

def is_balanced(tree_node):

     # We need to have a stack for DFS
    keep_depth = []
    keep_node_depth = []
    keep_node_depth.append((tree_node, 0))
    # Unitl the stack has elements we are not done and we need to still move forward (Traverse!)
    # Tree traversal
    while len(keep_node_depth) > 0:
        node, depth = keep_node_depth.pop()
        
        # In the case that we arrive to a new leaf we need to update the depth
        # Check if we arrive to a new leaf
        if (not node.left) and (not node.right):
            if depth not in keep_depth:
                keep_depth.append(depth)
            if (len(keep_depth) > 2) or (len(keep_depth) == 2 and (max(keep_depth) - min(keep_depth)) > 1):
                return False
        # If we have not arrived to a leaf yet
        if node.left:
            keep_node_depth.append((node.left, depth + 1))
        # Here as we append the right nodes last it traverse up to the end of each right leaf
        if node.right:
            keep_node_depth.append((node.right, depth + 1))
            
    return True
        
        
        



    