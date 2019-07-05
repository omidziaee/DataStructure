'''
Created on Apr 3, 2019

@author: USOMZIA
'''
class Solution(object):
    def maxDepth_stack(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 1
        stack_keep_nodes = []
        max_level = 0
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append((root, level))
                root = root.left
                if root:
                    level += 1
            else:
                node, level = stack_keep_nodes.pop()
                root = node.right
                if root:
                    level += 1
                max_level = max(max_level, level)
        return max_level
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
    
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
tree = TreeNode(3)
left = TreeNode(2)
right = TreeNode(5)
left_left = TreeNode(1)
left_right = TreeNode(4)
tree.left = left
tree.right = right
left.right = left_right
left.left = left_left

sol = Solution()
print sol.maxDepth(tree)