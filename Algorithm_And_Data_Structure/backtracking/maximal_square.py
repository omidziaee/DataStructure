'''
Created on Jul 19, 2019

@author: USOMZIA
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols + 1)]for _ in range(rows + 1)]
        max_sq_len = 0
        # ignore the first cell and start from 1 because of course it does not have
        # any prepheral cell around
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_sq_len = max(max_sq_len, dp[i][j])
        return max_sq_len ** 2

sol = Solution()
print sol.maximalSquare([["1"]])