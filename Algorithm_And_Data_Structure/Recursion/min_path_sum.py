'''
Created on Jun 16, 2019

@author: omid
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
## Dude without memoization it won't give you the result!!
class Solution():
    def __init__(self):
        self.memo = {}
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.find_min_path(grid, 0, 0)
    # time complexity is o(2^(n + m)) for each cell we have two options down or right
    # space complexity is o(n + m)
    def find_min_path(self, grid, i, j):
        # Base case easy case without any caluculation
        if j == len(grid[0]) - 1 and i == len(grid) - 1:
            return grid[i][j]
        # This is neseccary because of the i + 1 and j + 1 in returns
        if j > len(grid[0]) - 1 or i > len(grid) - 1:
            return float('inf')
        if (i, j) in self.memo:
            return self.memo[(i,j)]
        res = grid[i][j] + min(self.find_min_path(grid, i + 1, j), self.find_min_path(grid, i, j + 1))
        self.memo[(i, j)] = res
        return res