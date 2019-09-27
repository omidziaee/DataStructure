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
        # This one is necessary because at least we know that for each value the value minus that value is zero
        dic_cum_sum[0] = 1
        # We should use just one pass and fill both hashmap and check for the needed value at the same loop
        # similar to sum of two numbers if we do it in two separate loop and we have one value and the twice of it
        # we will get larger number
        for i in range(len(A)):
            cum_sum += A[i]
            needed = cum_sum % K
            if needed in dic_cum_sum:
                counter +=dic_cum_sum[needed]
                dic_cum_sum[needed] += 1
            else:
                dic_cum_sum[needed] = 1
        return counter

A = [4,5,0,-2,-3,1]
K = 5
sol = Solution()
print sol.subarraysDivByK(A, K)
                    
        