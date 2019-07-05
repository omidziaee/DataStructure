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
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[0][0] = 1
        for i in range(rows + 1):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
        for j in range(cols + 1):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1  
        for i in range(2, rows + 1):
            for j in range(2, cols + 1):
                if obstacleGrid[i][j] != 1: 
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print dp
        return dp[rows][cols]
sol = Solution()
print sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])