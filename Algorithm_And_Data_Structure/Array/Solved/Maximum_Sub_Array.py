'''
Created on Sep 27, 2018

@author: USOMZIA
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return 
its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArrNaive(self, nums):
        sumMax = 0
        for i in range(len(nums) - 1):
            sumTemp = nums[i]
            for j in range(i+1, len(nums)):
                sumTemp += nums[j]
                if sumTemp > sumMax:
                    sumMax = sumTemp
                    
        return sumMax
    def maxSub(self, nums):
        maxSum = nums[0]
        maxCurr = 0
        for i in range(len(nums)):
            maxCurr = max(maxCurr + nums[i], nums[i])
            maxSum = max(maxCurr, maxSum)
        return maxSum
            
    
    
sol = Solution()
print sol.maxSub([4,-1,2,1])
                    