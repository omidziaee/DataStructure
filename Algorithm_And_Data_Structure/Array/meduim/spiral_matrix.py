'''
Created on Aug 15, 2019

@author: USOMZIA
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution():
    def spiralOrder(self, nums):
        if not nums:
            return []
        ans = []
        # We need for pointers 
        r1 = c1 = 0
        r2, c2 = len(nums) - 1, len(nums[0]) - 1
        
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                ans.append(nums[r1][c])
            for r in range(r1 + 1, r2 + 1):
                ans.append(nums[r][c2])
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    ans.append(nums[r2][c])
                for r in range(r2, r1, -1):
                    ans.append(nums[r][c1])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return ans
    
nums = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
sol = Solution()
print sol.spiralOrder(nums)
