<<<<<<< HEAD
'''
Created on Mar 2, 2019

@author: omid
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
class Solution(object):
    def __init__(self):
        self.ans = 1
    def dfs(self, root):
        # pre order
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, right + left + 1)
        return left.val + right.val
        




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
=======
'''
Created on Mar 2, 2019

@author: omid
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
class Solution(object):
    def __init__(self):
        self.ans = 1
    def dfs(self, root):
        # pre order
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, right + left + 1)
        return left.val + right.val
        




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
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
sol.dfs(tree)