'''
Created on Sep 27, 2018

@author: USOMZIA
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the 
whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case
        if len(nums) <= 2:
            if nums[-1] < nums[0]:
                return 2
            else:
                return 0
        # We need to find the min and max values in the unsorted array
        min_in_unsorted = float('inf')
        max_in_unsorted = -float('inf')
        # left forward traverse to find the first position
        for left_traverse_index in range(1, len(nums)):
            if nums[left_traverse_index - 1] > nums[left_traverse_index]:
                # If we are here we know that the unsorted array has started
                min_in_unsorted = min(nums[left_traverse_index], min_in_unsorted)
        # right backward traverse to find the last position
        for right_traverse_index in range(len(nums) - 2, -1, -1):
            if nums[right_traverse_index] > nums[right_traverse_index + 1]:
                max_in_unsorted = max(nums[right_traverse_index], max_in_unsorted)
        # Now traverse in the main list to find the position of the min and max values of the unsorted list
        for left_index in range(len(nums)):
            if min_in_unsorted < nums[left_index]:
                break
        for right_index in range(len(nums) - 1, -1, -1):
            if max_in_unsorted > nums[right_index]:
                break
        # If the array is already fully sorted right index would be less than the left index
        return 0 if right_index < left_index else right_index - left_index + 1
    
    
    
sol = Solution()
nums = [1, 2, 3, 4]
print sol.findUnsortedSubarray(nums)