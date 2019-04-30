'''
Created on Apr 3, 2019

@author: USOMZIA
'''
class Solution(object):
    def maxDepth(self, root):
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