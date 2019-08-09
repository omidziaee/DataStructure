'''
Created on Aug 8, 2019

@author: USOMZIA
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution():
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using index as hash key
        # The largest min is for the case that if the length of the array is n it contains the number from 
        # 1 to n, in this case the minimum positive number is n + 1.
        # First check if there is no 1 in the array the minimum is 1
        one_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_counter += 1
        if one_counter == 0:
            return 1
        # Anyways if it has just one element and that one was not one it returns one on top otherwise it should 
        # return 2
        if len(nums) == 1:
            return 2
        # Convert all the negative and greater than len(n) to 1.
        for i in range(len(nums)):
            # Negative and larger than the len(nums) are useless.
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        # Now check the elements and use the index as the hash key(it is unique).
        # If the element is positive make it negative.
        for i in range(len(nums)):
            # as we use the a as index so it should be positive
            a = abs(nums[i])
            if a == len(nums):
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        # Now if an element is positive it means that no number with the index of that positive number in the list that cause this 
        # does not exist
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        # If it is in order series of numbers from 0 to len(nums) - 1
        if nums[0] > 0:
            return len(nums)
        return len(nums) + 1

nums =  [2,1]
sol = Solution()
print sol.firstMissingPositive(nums)