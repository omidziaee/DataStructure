<<<<<<< HEAD
'''
Created on Mar 7, 2019

@author: omid
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
class Solution():
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 0
        depth = 1
        stack_keep_nodes = []
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append((root, depth))
                if not root.right and not root.left:
                    max_depth = max(max_depth, depth)
                root = root.left
                if root:
                    depth += 1
            else:
                node, depth = stack_keep_nodes.pop()
                root = node.right
                if root:
                    depth += 1
        return max_depth
    
    def maxDepth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # Recursively traverse left and right and for each left and right add one just find the max depth
        return 1 + max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right))
    
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

tree = TreeNode(5)
right = TreeNode(13)
left = TreeNode(2)
tree.right = right
tree.left = left

sol = Solution()
=======
'''
Created on Mar 7, 2019

@author: omid
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
class Solution():
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 0
        depth = 1
        stack_keep_nodes = []
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append((root, depth))
                if not root.right and not root.left:
                    max_depth = max(max_depth, depth)
                root = root.left
                if root:
                    depth += 1
            else:
                node, depth = stack_keep_nodes.pop()
                root = node.right
                if root:
                    depth += 1
        return max_depth
    
    def maxDepth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # Recursively traverse left and right and for each left and right add one just find the max depth
        return 1 + max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right))
    
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

tree = TreeNode(5)
right = TreeNode(13)
left = TreeNode(2)
tree.right = right
tree.left = left

sol = Solution()
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print sol.maxDepth_recursive(tree)