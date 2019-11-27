'''
Created on Jan 23, 2019

@author: USOMZIA
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally
 (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
# This is a recursive DFS
class Solution():
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, self.helper(grid, seen, i, j))
        return ans
    def helper(self, grid, seen, row, col):
        # Base case easy case
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or (row, col) in seen or grid[row][col] == 0:
            return 0
        seen.add((row, col))
        return 1 \
                + self.helper(grid, seen, row + 1, col)\
                + self.helper(grid, seen, row - 1, col)\
                + self.helper(grid, seen, row, col + 1)\
                + self.helper(grid, seen, row, col - 1)
                
grid = [[1,0,0], [0,0,0], [0,0,0]]
sol = Solution()
print sol.maxAreaOfIsland(grid)