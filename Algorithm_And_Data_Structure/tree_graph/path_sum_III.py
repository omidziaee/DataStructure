'''
Created on May 10, 2019

@author: omid
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
class BinaryTree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def __init__(self):
        self.counter = 0
    def pathSum(self, root, sum):
        if not root:
            return 0
        self.dfs(root, sum)
        return self.counter
    
    def dfs(self, root, target):
        if not root:
            return 0
        self.dfs(root.left, target)
        self.second_dfs(root, target)
        self.dfs(root.right, target)
        
    def second_dfs(self, root, target):
        if not root:
            return 0
        if root.val == target:
            self.counter += 1
        self.second_dfs(root.left, target - root.val)
        self.second_dfs(root.right, target - root.val)
    
tree = BinaryTree(10)
left = BinaryTree(5)
right = BinaryTree(-3)
right_right = BinaryTree(11)
left_right = BinaryTree(2)
left_left = BinaryTree(3)
left_right_right = BinaryTree(1)
left_left_right = BinaryTree(-2)
left_left_left = BinaryTree(3)
tree.right = right
tree.left = left
right.right = right_right
left.right = left_right
left.left = left_left
left.right.right = left_right_right
left.left.right = left_left_right
left.left.left = left_left_left

sol = Solution()
print sol.pathSum(tree, 8)