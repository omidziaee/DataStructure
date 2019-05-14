'''
Created on May 14, 2019

@author: omid
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''
class BinaryTree():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        import collections
        if not root:
            return []
        queue_keep = collections.deque()
        level = 0
        queue_keep.append((root, level))
        # The dictionary is in order to keep the levels and values
        keep_levels = {}
        while queue_keep:
            node, level = queue_keep.popleft()
            if level in keep_levels:
                keep_levels[level].append(node.val)
            else:
                keep_levels[level] = [node.val]
            if node.left:
                queue_keep.append((node.left, level + 1))
            if node.right:
                queue_keep.append((node.right, level + 1))
        res = [None for _ in range(len(keep_levels))]
        for key in keep_levels:
            # Do not forget to put float in here otherwise it just returns the int part
            res[key] = float(sum(keep_levels[key])) / len(keep_levels[key])
        return res
    
tree = BinaryTree(3)
left = BinaryTree(9)
right = BinaryTree(20)
right_left = BinaryTree(15)
right_right = BinaryTree(7)
tree.left = left
tree.right = right
right.right = right_right
right.left = right_left

sol = Solution()
print sol.averageOfLevels(tree)

