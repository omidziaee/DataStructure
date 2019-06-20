'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # The idea is not very simple but we know if nums[i] > nums[i + 1] happens more than once 
        # we need to return False. So we keep track of number of times that nums[i] > nums[i + 1] 
        # happens with a flag! If it happens at 0 or len(nums) - 2 it is possible to change it to 
        # nums[1] or nums[len(nums) - 1]. If it happens other places (call it p) we need to check 
        # either nums[p - 1] < nums[p + 1] (then we can change nums[p] to nums[p + 1]) or nums[p] < nums[p + 2] 
        # (then we can change nums[p + 1] to nums[p + 2]).
        # In any case we just need to check the elements close to element that nom monotonocity happens around it.
        place_of_non_monotonicity = None
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                # if it is not None it means it happened before
                if place_of_non_monotonicity != None:
                    return False
                # The first time it happened we keep the index 
                place_of_non_monotonicity = index
        return ((place_of_non_monotonicity == None) or \
        (place_of_non_monotonicity == 0) or \
        (place_of_non_monotonicity == len(nums) - 2) or \
        (nums[place_of_non_monotonicity - 1] < nums[place_of_non_monotonicity + 1]) or \
        (nums[place_of_non_monotonicity] < nums[place_of_non_monotonicity + 2]))
