'''
Created on Aug 15, 2019

@author: USOMZIA
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution():
    def generateMatrix(self, n):
        if n == 0:
            return []
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        # for pointers
        r1 = c1 = 0
        r2, c2 = len(ans) - 1, len(ans[0]) - 1
        i = 1
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                ans[r1][c] = i
                i += 1
            for r in range(r1 + 1, r2 + 1):
                ans[r][c2] = i
                i += 1
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    ans[r2][c] = i
                    i += 1
                for r in range(r2, r1, -1):
                    ans[r][c1] = i
                    i += 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return ans
    
sol = Solution()
print sol.generateMatrix(3)
                    