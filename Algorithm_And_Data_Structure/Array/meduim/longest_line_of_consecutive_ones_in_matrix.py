'''
Created on Oct 23, 2019

@author: omid
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, 
vertical, diagonal or anti-diagonal.
Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
'''
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        dp = [[[0,0,0,0] for _ in range(len(M[0]) + 1)] for k in range(len(M) + 1)]
        max_len = 0
        for i in range(len(M) - 1, -1, -1):
            for j in range(len(M[0]) - 1, -1, -1):
                if M[i][j] == 1:
                    dp[i][j][0] = dp[i + 1][j][0] + 1
                    dp[i][j][1] = dp[i][j + 1][1] + 1
                    dp[i][j][2] = dp[i + 1][j + 1][2] + 1
                    dp[i][j][3] = dp[i + 1][j - 1][3] + 1
                max_len = max(max_len, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return max_len
                 
        