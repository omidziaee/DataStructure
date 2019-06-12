'''
Created on May 17, 2019

@author: omid
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
    # Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
class Solution(object):
    def __init__(self):
        self.dic_count = {}
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        # When you are looking for max this should be a really small number 
        # When you are looking for min this should be a really large number
        mode = -float('inf')
        res = []
        for value in self.dic_count.values():
            mode = max(mode, value)
        for key, value in self.dic_count.items():
            if value == mode:
                res.append(key)
        return res
    
    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.left)
        if root.val in self.dic_count:
            self.dic_count[root.val] += 1
        else:
            self.dic_count[root.val] = 1
        self.dfs(root.right)
        
tree = TreeNode(1)
right = TreeNode(2)
right_left = TreeNode(2)
tree.right = right
right.left = right_left
sol = Solution()
print sol.findMode(tree)