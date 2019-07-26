'''
Created on Jul 9, 2019

@author: USOMZIA
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    class Solution(object):
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        self.dfs(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root               

    
root = TreeNode(1)
right = TreeNode(5)
left = TreeNode(2)
right_right = TreeNode(6)
left_right = TreeNode(4)
left_left = TreeNode(3)
root.right = right
root.left = left
right.right = right_right
left.right = left_right
left.left = left_left
sol = Solution()
print sol.flatten(root)

        