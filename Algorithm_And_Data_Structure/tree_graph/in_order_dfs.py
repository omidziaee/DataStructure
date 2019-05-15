<<<<<<< HEAD
'''
Created on Mar 2, 2019

@author: omid
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
class Solution(object):
    def inorderTraversal_recursive_simple(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 
    
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
     
    def inorderTraversal(self, root): 
        if not root:
            return []
        stack_keep_nodes = []
        stack_keep_values = []
        
        #outer loop to keep the traverse over all the node it will get out whenever stack is empty
        while 1:
            # Now traverse over all the left nodes
            while root:
                stack_keep_nodes.append(root)
                root = root.left  
            # Check if the stack is empty get out of the outer loop
            if not stack_keep_nodes:
                return stack_keep_values
            # Now pop from the top of the stack
            node = stack_keep_nodes.pop()
            stack_keep_values.append(node.val)
            root = node.right
        
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
# tree = TreeNode(1)
# right = TreeNode(2)
# right_left = TreeNode(3)
# tree.right = right
# right.left = right_left
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
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
class Solution(object):
    def inorderTraversal_recursive_simple(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 
    
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return res
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
     
    def inorderTraversal(self, root): 
        if not root:
            return []
        stack_keep_nodes = []
        stack_keep_values = []
        
        #outer loop to keep the traverse over all the node it will get out whenever stack is empty
        while 1:
            # Now traverse over all the left nodes
            while root:
                stack_keep_nodes.append(root)
                root = root.left  
            # Check if the stack is empty get out of the outer loop
            if not stack_keep_nodes:
                return stack_keep_values
            # Now pop from the top of the stack
            node = stack_keep_nodes.pop()
            stack_keep_values.append(node.val)
            root = node.right
        
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
# tree = TreeNode(1)
# right = TreeNode(2)
# right_left = TreeNode(3)
# tree.right = right
# right.left = right_left
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
print sol.inorderTraversal(tree)