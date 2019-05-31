'''
Created on May 21, 2019

@author: omid
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def __init__(self):
        self.dic_keep_index = {}
        self.istwo = False
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dfs(root, k)
        return self.istwo
    def dfs(self, root, target):
        # we need them sorted so in_order
        if not root:
            return False
        self.dfs(root.left, target)
        if target - root.val in self.dic_keep_index:
            self.istwo = True
        else:
            self.dic_keep_index[root.val] = 1
        self.dfs(root.right, target)
        
    def findTarget_2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tree_values = []
        self.dfs_2(root, tree_values)
        res = self.two_sum(tree_values, k)
        return res
    def dfs_2(self, root, tree_values):
        # we need them sorted so in_order
        if not root:
            return []
        self.dfs(root.left, tree_values)
        tree_values.append(root.val)
        self.dfs(root.right, tree_values)
    def two_sum(self, nums, target):
        dic_keep_index = {}
        for i in range(len(nums)):
            if target - nums[i] in dic_keep_index:
                return True
            else:
                dic_keep_index[nums[i]] = i
        return False
        
tree = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
tree.left = left
tree.right = right
sol = Solution()
print sol.findTarget(tree, 4)
