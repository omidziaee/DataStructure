'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    def findMissing(self, nums):
        maxElem = len(nums)
        aSum = 0
        mainSum = maxElem * (maxElem + 1) / 2
        for elem in nums:
            aSum += elem
        return mainSum - aSum
    
sol = Solution()
print sol.findMissing([9,6,4,2,3,5,7,0,1])
        