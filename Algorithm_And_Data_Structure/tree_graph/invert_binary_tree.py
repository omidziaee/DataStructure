'''
Created on Feb 12, 2019

@author: USOMZIA
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def invert_tree_recursive(self, root):
        #base case
        if not root:
            return root
        # Goes all the way down at first iteration right_node is None and the root is 9 left_node is also None
        # So at the first iteration it swaps the None and None node. Then it goes one level up. 
        right_node = self.invert_tree_recursive(root.right)
        left_node = self.invert_tree_recursive(root.left)
        
        root.left = right_node
        root.right = left_node
        
        return root
    
    
    def invert_tree(self, root):
        if not root:
            return root
        # Now do it with BFS and a queue
        import collections
        keep_nodes = collections.deque()
        keep_nodes.append(root)
        while keep_nodes:
            curr_node = keep_nodes.popleft()
            # This is the only difference between this and the BFS
            # Now swap the right and left node it does not matter if one of them is empty as we just
            # intend to swap the right and left nodes
            temp = curr_node.right
            curr_node.right = curr_node.left
            curr_node.left = temp
            # swap finished
            # Now it is time to add the new nodes to the queue. Bear in mind that we do not want to 
            # add empty nodes to the queue so first we check if it is empty then we skip
            if curr_node.left:
                keep_nodes.append(curr_node.left)
            if curr_node.right:
                keep_nodes.append(curr_node.right)
                
        return root
    
tree_node = TreeNode(4)
tree_right = TreeNode(7)
tree_left = TreeNode(2)
tree_right_right = TreeNode(9)
tree_right_left = TreeNode(6)
tree_left_left = TreeNode(1)
tree_left_right = TreeNode(3)
tree_node.right = tree_right
tree_node.left = tree_left
tree_right.right = tree_right_right
tree_right.left = tree_right_left
tree_left.right = tree_left_right
tree_left.left = tree_left_left

sol = Solution()
print sol.invert_tree(tree_node)
