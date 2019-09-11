'''
Created on Sep 5, 2019

@author: USOMZIA
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping
 (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could
  occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
'''
class Solution():
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = dp[i - 1] + A[i]
        res, max_L, max_M = dp[L + M - 1], dp[L - 1], dp[M - 1]
        for i in range(L + M, len(A)):
            # Whatever now and shift one forward
            max_L = max(max_L, dp[i - M] - dp[i - L - M])
            max_M = max(max_M, dp[i - L] - dp[i - L - M])
            # Now either max_L is first 
            res = max(res, max_L + dp[i] - dp[i - M], max_M + dp[i] - dp[i - L])
        return res

A = [2,1,5,6,0,9,5,0,3,8] 
L = 4
M = 3   
sol = Solution()
print sol.maxSumTwoNoOverlap(A, L, M)
    