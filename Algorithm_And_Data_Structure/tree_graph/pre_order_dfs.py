'''
Created on Mar 2, 2019

@author: omid
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

class Solution(object):
    def preorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack_keep_nodes = []
        keep_values = []
        stack_keep_nodes.append(root)
        while stack_keep_nodes:
            node = stack_keep_nodes.pop()
            node_value = node.val
            keep_values.append(node_value)
            if node.right:
                stack_keep_nodes.append(node.right)
            if node.left:
                stack_keep_nodes.append(node.left)
        return keep_values
    # recursive
    def preorderTraversal_general_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
    
    def preorderTraversal(self, root):
        if not root:
            return []
        # The idea is similar to what it is done for string reverse with recursion but the important thing is 
        # to put the first one in []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)   
        
        
        
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
tree = TreeNode(1)
right = TreeNode(2)
right_left = TreeNode(3)
tree.right = right
right.left = right_left

sol = Solution()
print sol.preorderTraversal(tree)
