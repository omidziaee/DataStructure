'''
Created on Aug 30, 2019

@author: USOMZIA
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  
The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
'''
class Solution(object):
    def maxWidthRamp_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_width = -float("inf")
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[j] >= A[i]:
                    max_width = max(max_width, j - i)
        return max_width if max_width != -float("inf") else 0
    
    def maxWidthRamp(self, A):
        ans = 0
        minimum_index_so_far = float("inf")
        for i in sorted(range(len(A)), key = lambda i:A[i]):
            ans = max(ans, i - minimum_index_so_far)
            # Now update the minimum index so far
            minimum_index_so_far = min(minimum_index_so_far, i)
        return ans
            
A = [9,8,1,0,1,9,4,0,4,1]
sol = Solution()
print sol.maxWidthRamp(A)