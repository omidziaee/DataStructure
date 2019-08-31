'''
Created on Aug 21, 2019

@author: omid
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
To undestand it better consider the matrix like:
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
now it is obvious it is DP and you can solve it etiher from top or from bottom
'''
class Solution():
    # O(n*n/2) space, top-down 
    def minimumTotal1_from_top(self, triangle):
        if not triangle:
            return None
        # look how row is being defined it is great!!
        dp = [[0 for _ in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                if j == len(triangle) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])
    
    def minimumTotal_from_bottom(self, triangle):
        if not triangle:
            return None
        for i in range(len(triangle) - 2, -1, -1):
            # We do not use extra space just use the original matrix
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j + 1], triangle[i + 1][j])
                
        return triangle[0][0]
                
        