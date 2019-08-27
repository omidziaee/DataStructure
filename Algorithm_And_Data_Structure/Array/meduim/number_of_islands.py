'''
Created on Aug 22, 2019

@author: USOMZIA
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed
by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == 1:
                    self.helper(grid, seen, i, j)
                    ans += 1
        return ans
    def helper(self, grid, seen, row, col):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or (row, col) in seen or grid[row][col] == 0:
            return 
        seen.add((row, col)) # if it says in place here change the grid[row][col] = "#" or anything distinguishable even '0' is fine.
        self.helper(grid, seen, row + 1, col)
        self.helper(grid, seen, row - 1, col)
        self.helper(grid, seen, row, col + 1)
        self.helper(grid, seen, row, col - 1)
        
                
grid = [[1,1,0], [1,1,0], [0,0,0]]               
sol = Solution()
print sol.numIslands(grid)
                
