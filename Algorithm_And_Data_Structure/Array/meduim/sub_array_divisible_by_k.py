'''
Created on Sep 26, 2019

@author: USOMZIA
Given an array A of integers, return the number of (contiguous, non-empty) 
subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
'''
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dic_cum_sum = {}
        cum_sum = 0
        counter = 0
        for i in range(len(A)):
            cum_sum += A[i]
            dic_cum_sum[i] = cum_sum
        max_div = cum_sum / K
        for i in range(max_div):
            if dic_cum_sum - K * i in dic_cum_sum:
                counter += 1
                    
        