'''
Created on Jul 31, 2019

@author: USOMZIA
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        first = lower - 1
        nums.append(upper + 1)
        for i in range(len(nums)):
            if nums[i] - first == 2:
                res.append("%d" %(nums[i] - 1))
            elif nums[i] - first > 2:
                res.append("%d->%d" %(first + 1, nums[i] - 1))
            first = nums[i]
        return res