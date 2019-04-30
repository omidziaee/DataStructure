'''
Created on Feb 20, 2019

@author: USOMZIA
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # This is the recursive approach 
    # The idea is to look at the tree like a mirror 
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # The idea is to mirroring the tree; meaning decompose it to two tree
        # then the right of first should be equal to the left of the second one
        import collections
        queue_keep_nodes = collections.deque()
        queue_keep_nodes.append(root)
        queue_keep_nodes.append(root)
        while queue_keep_nodes:
            # Pop left twice you can do it by adding a tuppele and in the tupple 
            # out this two and pop just once
            node1 = queue_keep_nodes.popleft()
            node2 = queue_keep_nodes.popleft()
            # This is for the last node and it should be here
            if (not node1 and not node2):
                continue
            if (not node1 or not node2):
                return False
            # Check if the value of mirrors are not equal
            if (node1.val != node2.val):
                return False
            # Now it is time to add to the queue but in a special manner bear in mind the
            # order is very important
            # No need to check for teh emptyness
            # The two end edges
            # We need four push as we basically use two trees two for each tree
            queue_keep_nodes.append(node1.left)
            queue_keep_nodes.append(node2.right)
            queue_keep_nodes.append(node1.right)
            queue_keep_nodes.append(node2.left)
        return True
    def isSymetric_recursive(self, root):
        # for the recursive we need to send two trees and compare them
        # so we need another helper function with two inouts
        return self.isSymetric_helper(root, root)
    
    def isSymetric_helper(self, node1, node2):
        # Base case
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        # As we basically deal with two trees we need two recursive
        return node1.val == node2.val and self.isSymetric_helper(node1.left, node2.right) and self.isSymetric_helper(node1.right, node2.left)
        

        
class BinaryTree():
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None
        
        
tree = BinaryTree(1)
left = BinaryTree(2)
right = BinaryTree(2)
left_left = BinaryTree(3)
left_right = BinaryTree(4)
right_left = BinaryTree(4)
right_right = BinaryTree(3)
tree.left = left
tree.right = right
left.left = left_left
left.right = left_right
right.right = right_right
right.left = right_left        

sol = Solution()
print sol.isSymetric_recursive(tree)
        