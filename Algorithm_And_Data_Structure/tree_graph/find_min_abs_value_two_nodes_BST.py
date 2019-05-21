'''
Created on May 17, 2019

@author: omid
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree_list = []
        self.dfs(root, tree_list)
        tree_list.sort()
        min_diff = float('inf')
        '''
        # This is o(n^2)
        for i in range(len(tree_list)):
            for j in range(i + 1, len(tree_list)):
                min_diff = min(abs(tree_list[j] - tree_list[i]), min_diff)
        return min_diff
        '''
        # The following is o(nlgn)
        # or in place tree_list.sort()
        sort_tree = sorted(tree_list)
        for i in range(len(sort_tree) - 1):
            min_diff = min(min_diff, sort_tree[i + 1] - sort_tree[i])
        return min_diff
        
    
    def dfs(self, root, tree_list):
        if not root:
            return []
        # Inorder
        self.dfs(root.left, tree_list)
        tree_list.append(root.val)
        self.dfs(root.right, tree_list)
