'''
Created on Oct 22, 2019

@author: omid
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        set_delete = set(to_delete)
        res = []
        self.helper(root, res, set_delete, True)
        return res
    def helper(self, root, res, set_delete, root_deleted):
        if not root:
            return None
        # This is a binary variable to indicate either the value is in to_delete set
        is_root = root.val in set_delete
        if not is_root or root_deleted:
            res.append(root)
        self.helper(root.left, res, set_delete, is_root)
        self.helper(root.right, res, set_delete, is_root)
        return None if is_root else root
        