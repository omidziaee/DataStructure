'''
Created on Mar 29, 2020

@author: omid
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        summ = 0
        maxlen = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic:
                maxlen = max(maxlen, i-dic[summ-k])
            # It should be like this else does not work because else updates the last one
            # and as we want the max we should not update the last one
            if summ not in dic:
                dic[summ] = i
        return maxlen