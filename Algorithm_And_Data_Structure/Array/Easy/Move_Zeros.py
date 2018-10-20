'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeros(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.insert(len(nums), nums[i])
                nums.pop(i)
        return nums

sol = Solution()
print sol.moveZeros([0,1,0,3,12, 15, 0])