'''
Created on Jul 19, 2019

@author: USOMZIA
'''
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution():
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
    #--------------------------------------------
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        return self.helper(preorder, inorder, dic)
    def helper(self, preorder, inorder, dic):
        if len(preorder) == 0:
            return None
        else:
            root = TreeNode(preorder.pop(0))
            ind = dic[root.val]
            root.left = self.helper(preorder, inorder[:ind], dic)
            root.right = self.helper(preorder, inorder[ind + 1:], dic)
        return root
        
root = TreeNode(3)
right = TreeNode(20)
left = TreeNode(9)
left_left = TreeNode(4)
left_right = TreeNode(3)
right_left = TreeNode(15)
right_right = TreeNode(7)
root.right = right
root.left = left
right.right = right_right
right.left = right_left
#left.right = left_right
#left.left = left_left

inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]
sol = Solution()
print sol.buildTree(preorder, inorder)


        