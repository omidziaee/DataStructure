<<<<<<< HEAD
'''
Created on Apr 19, 2019

@author: omid
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''
class Solution():
    def __init__(self):
        self.total_sum = 0
    def convertBST(self, root):
        # You can not send a total sum from here to the lower level function
        # It is wrong as when it goes back to the previous state total_sum 
        # change to zero again and cause issue
        #total_sum = 0
        # We need a global memory that at each recursion can get updated 
        # That is just possible if we set in the constructor
        return self.dfs(root)
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        self.total_sum += root.val
        root.val = self.total_sum
        self.dfs(root.left)
        return root
    
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
tree = TreeNode(5)
left = TreeNode(2)
right = TreeNode(13)
tree.left = left
tree.right = right

sol = Solution()
=======
'''
Created on Apr 19, 2019

@author: omid
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''
class Solution():
    def __init__(self):
        self.total_sum = 0
    def convertBST(self, root):
        # You can not send a total sum from here to the lower level function
        # It is wrong as when it goes back to the previous state total_sum 
        # change to zero again and cause issue
        #total_sum = 0
        # We need a global memory that at each recursion can get updated 
        # That is just possible if we set in the constructor
        return self.dfs(root)
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        self.total_sum += root.val
        root.val = self.total_sum
        self.dfs(root.left)
        return root
    
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
tree = TreeNode(5)
left = TreeNode(2)
right = TreeNode(13)
tree.left = left
tree.right = right

sol = Solution()
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print sol.convertBST(tree)