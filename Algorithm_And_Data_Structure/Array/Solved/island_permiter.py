'''
Created on Apr 23, 2019

@author: USOMZIA
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
 is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with
 side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        one_counter = 0
        one_negibor_counter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    one_counter += 1
                    if row > 0: # and gird[row - 1][col] == 1
                        if grid[row - 1][col] == 1:
                            one_negibor_counter += 1
                    if col > 0:
                        if grid[row][col - 1] == 1:
                            one_negibor_counter += 1
        return 4 * one_counter - 2 * one_negibor_counter
        
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]        
sol = Solution()
print sol.islandPerimeter(grid)