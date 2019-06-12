'''
Created on Jun 6, 2019

@author: USOMZIA
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
class Solution():
    def __init__(self):
        self.keep_node = {}
    # The level traversal should work without any doubt
    def rob_level_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        import collections
        deque_keep = collections.deque()
        dic_level_keep = {}
        deque_keep.append([root, 1])
        while deque_keep:
            root, level = deque_keep.popleft()
            if level in dic_level_keep:
                dic_level_keep[level].append(root.val)
            else:
                dic_level_keep[level] = [root.val]
            if root.left:
                deque_keep.append([root.left, level + 1])
            if root.right:
                deque_keep.append([root.right, level + 1])
        # Now it is like the staircase
        level_value = [0 for _ in range(level)]
        for key, values in dic_level_keep.items():
            level_value[key - 1] = sum(values)
        dp = [float('inf') for _ in range(level)]
        dp[0] = level_value[0]
        dp[1] = max(level_value[0], level_value[1])
        for i in range(2, level):
            dp[i] = max(dp[i - 1], level_value[i] + dp[i - 2])
        return dp[level - 1]
    def rob(self, root, indent):
        if root:
            print indent + "checking root %d" %root.val
        if not root:
            return 0
        if root in self.keep_node:
            return self.keep_node[root]
        val = 0
        if root.left:
            val += self.rob(root.left.left, indent + "  ") + self.rob(root.left.right, indent + "  ")
        if root.right:
            val += self.rob(root.right.left, indent + "  ") + self.rob(root.right.right, indent + "  ")
        res = max(val + root.val, self.rob(root.left, indent + "  ") + self.rob(root.right, indent + "  "))
        self.keep_node[root] = res
        return res
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        
tree = TreeNode(6)
left = TreeNode(4)
right = TreeNode(5)
left_left = TreeNode(1)
left_right = TreeNode(3)
right_left = TreeNode(7)
right_right = TreeNode(9)
tree.right = right
tree.left = left
left.left = left_left
left.right = left_right
right.right = right_right
right.left = right_left

sol = Solution()
print sol.rob(tree, "")
            
        
            
