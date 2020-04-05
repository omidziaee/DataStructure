'''
Created on Jun 25, 2019

@author: omid
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                # If the cell in row 0 is an obstacle from that cell onward it is not possible to move
                for k in range(j, cols):
                    dp[0][k] = 0
                break
        for i in range(rows):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                # The same for the previous one if one cell in the column 0 is an obstackle it is not possible to move on
                for k in range(i, rows):
                    dp[k][0] = 0
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[rows - 1][cols - 1]

grid = [[0,1,0,0,0,1,0,0,0,0,1,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,1,0],[0,1,1,1,0,1,0,1,1,0,0,1,1,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,1,1,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,1,0,1,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,1,0,0],[1,0,0,0,1,0,1,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0],[0,1,1,1,0,0,0,0,0,0,1,1,1,0],[1,1,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,1,0],[0,1,0,0,0,0,0,1,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,1,0,0,0,1,0,0,0,1,0,1,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0],[1,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,1,0],[0,0,1,0,0,0,0,0,0,1,1,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0]]
sol = Solution()
print sol.uniquePathsWithObstacles(grid)