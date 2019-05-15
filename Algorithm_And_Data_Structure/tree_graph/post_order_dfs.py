'''
Created on Mar 5, 2019

@author: omid
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
class Solution():
    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return []
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        
    def postorderTraversal_recursive_simple(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    





class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
# tree = TreeNode(1)
# right = TreeNode(2)
# right_left = TreeNode(3)
# tree.right = right
# right.left = right_left
tree = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
tree.left = left
tree.right = right
left_left = TreeNode(4)
left_right = TreeNode(5)
left.left = left_left
left.right = left_right

sol = Solution()
print sol.postorderTraversal(tree)