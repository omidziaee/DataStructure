'''
Created on Aug 23, 2019

@author: omid
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i]
 when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray 
C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
'''
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Either the max sum is in the middle which is the Kadens algorithm or a part of 
        # it is in the begining and a part of it is the tail!
        # for the case that a part of it is at the end and a part at the begining, we need to 
        # decrease the whole_sum minus the min_sum in the middle!
        # https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
        curr_sum_max, curr_sum_min, min_sum, max_sum, whole_sum = 0, 0, float('inf'), -float('inf'), 0
        for i, elem in enumerate(A):
            curr_sum_max = max(curr_sum_max + elem, elem)
            max_sum = max(max_sum, curr_sum_max)
            curr_sum_min = min(curr_sum_min + elem, elem)
            min_sum = min(min_sum, curr_sum_min)
            whole_sum += elem
        # if max_sum is negative then whole_sum - min_sum is going to be zero
        return max(max_sum, whole_sum - min_sum) if max_sum > 0 else max_sum







