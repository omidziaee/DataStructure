'''
Created on Aug 24, 2019

@author: omid
80. Remove Duplicates from Sorted Array II
Medium

735

570

Favorite

Share
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
'''
class Solution(object):
    def removeDuplicates_just_length(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_final = len(nums)
        i = 0
        while i < len(nums):
            counter = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                counter += 1
                i += 1
            if counter > 2:
                len_final = len_final - counter + 2
            i += 1
        return len_final
    
    def removeDuplicates(self, nums):
        # Two pointers
        if not nums:
            return 0
        lst_non_repeating_indx = 0
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                lst_non_repeating_indx += 1
                nums[lst_non_repeating_indx] = nums[i]
                counter = 1
            else:
                if counter < 2:
                    lst_non_repeating_indx += 1
                    counter += 1
                    nums[lst_non_repeating_indx] = nums[i]
        return lst_non_repeating_indx + 1
                
            
        
nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
print sol.removeDuplicates(nums)
            









