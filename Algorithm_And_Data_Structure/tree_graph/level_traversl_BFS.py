'''
Created on Mar 5, 2019

@author: omid
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        if not root:
            return []
        queue_keep_nodes = collections.deque()
        level = 0
        queue_keep_nodes.append((level, root))
        keep_values = {}
        while queue_keep_nodes:
            level, root = queue_keep_nodes.popleft()
            if level in keep_values:
                keep_values[level].append(root.val)
            else:
                keep_values[level] = [root.val]
            if root.left:
                queue_keep_nodes.append((level + 1, root.left))
            if root.right:
                queue_keep_nodes.append((level + 1, root.right))
        res = [None for _ in range(len(keep_values))]
        for key in keep_values:
            res[key] = keep_values[key]
        return res

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
tree = TreeNode(3)
left = TreeNode(9)
right = TreeNode(20)
right_left = TreeNode(15)
right_right = TreeNode(7)
left_left = TreeNode(100)
left_right = TreeNode(200)
tree.left = left
tree.right = right
right.left = right_left
right.right = right_right
left.left = left_left
left.right = left_right

sol = Solution()
print sol.levelOrder(tree)