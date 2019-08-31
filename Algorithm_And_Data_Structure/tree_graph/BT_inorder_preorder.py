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
    def buildTree_pp(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        root_index = 0
        return self.helper(preorder, 0, len(inorder) - 1, dic, root_index)
    def helper_pp(self, preorder, left_index, right_index, dic, root_index):
        if left_index == right_index or root_index >= len(preorder) - 1:
            return None
        root_val = preorder[root_index]
        index = dic[root_val]
        root = TreeNode(root_val)
        root.left = self.helper(preorder, left_index, index, dic, root_index + 1)
        root.right = self.helper(preorder, index, right_index, dic, root_index + 1)
        return root
    def buildTree_slice(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rootValue = preorder.pop(0)
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        in_end = len(preorder) - 1
        return self.helper(preorder, inorder, in_end)
    def helper(self, preorder, inorder, in_end, in_start = 0, pre_start = 0, pre_end = None):
        if in_start > in_end:
            return None
        
        root = TreeNode(preorder[pre_start])
        if in_end == in_start:
            return root
        ind = inorder.index(root.val)
        root.left = self.helper(preorder, inorder, ind - 1, in_start, pre_start + 1)
        root.right = self.helper(preorder, inorder, in_end, ind + 1, pre_start + ind + 1 - in_start)
        return root

inorder = [4, 5, 6, 7, 2, 1, 8, 9, 3, 10]
preorder = [1, 2, 4, 5, 7, 6, 3, 8, 9, 10]
sol = Solution()
root_new = sol.buildTree(preorder, inorder)
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

#sol = Solution()
#print sol.print_nodes(root)





        