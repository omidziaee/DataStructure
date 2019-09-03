'''
Created on Aug 27, 2019

@author: USOMZIA
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def print_nodes(self, root):
        if not root:
            print "nothing to print"
        res = []
        self.dfs_preorder(root, res)
        return res
    def dfs_inorder(self, root, res):
        if not root:
            return res
        self.dfs_inorder(root.left, res)
        res.append(root.val)
        self.dfs_inorder(root.right, res)
    def dfs_preorder(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.dfs_preorder(root.left, res)
        self.dfs_preorder(root.right, res)
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
        
        
        
inorder = [4, 5, 6, 7, 2, 1, 8, 9, 3, 10]
postorder = [7, 5, 4, 6, 2, 9, 8, 10, 3, 1]
sol = Solution()
root_new = sol.buildTree(inorder, postorder)
print sol.print_nodes(root_new)


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left_left = TreeNode(4)
left_left_left = TreeNode(5)
left_left_right = TreeNode(6)
left_left_left_right = TreeNode(7)
right_left = TreeNode(8)
right_left_right = TreeNode(9)
right_right = TreeNode(10)
root.left = left
root.right = right
left.left = left_left
left.left.left = left_left_left
left.left.right = left_left_right
left.left.left.right = left_left_left_right
right.left = right_left
right.left.right = right_left_right
right.right = right_right





