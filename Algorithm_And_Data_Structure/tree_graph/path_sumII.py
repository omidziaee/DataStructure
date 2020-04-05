'''
Created on Aug 11, 2019

@author: omid
'''
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Solution():
    def pathSum(self, root, sum):
        if not root:
            return None
        res, curr_path = [], []
        self.dfs(root, res, curr_path, sum)
        return res
    def dfs(self, root, res, curr_path, sum):
        if (not root.left and not root.right and sum == root.val):
            curr_path.append(root.val)
            res.append(curr_path)
        if (root.left):
            self.dfs(root.left, res, curr_path + [root.val], sum - root.val)
        if (root.right):
            self.dfs(root.right, res, curr_path + [root.val], sum - root.val)
            
        
root = TreeNode(5)
right = TreeNode(8)
left = TreeNode(4)
left_left = TreeNode(11)
left_left_left = TreeNode(7)
left_left_right = TreeNode(2)
right_right = TreeNode(4)
right_left = TreeNode(13)
right_right_left = TreeNode(5)
right_right_right = TreeNode(1)
root.right = right
root.left = left
left.left = left_left
left.left.left = left_left_left
left.left.right = left_left_right
right.right = right_right
right.left = right_left
right.right.left = right_right_left
right.right.right = right_right_right


sol = Solution()
print sol.pathSum(root, 22)