'''
Created on Jun 18, 2019

@author: USOMZIA
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        smaller = 0
        larger = len(nums) - 1
        # first; forward traverse to move all the smaller than pivot to the front
        for i in range(len(nums)):
            if nums[i] < pivot:
                temp = nums[i]
                nums[i] = nums[smaller]
                nums[smaller] = temp
                # Now advance the smaller one more
                smaller += 1
        # second; backward traverse to move all the larger than pivot to the end
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > pivot:
                temp = nums[i]
                nums[i] = nums[larger]
                nums[larger] = temp
                larger -= 1
    def sortColors_one_pass(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        # divide the list into four sections 1)unclassified 2)smaller 3)equal 4)larger
        # smaller->nums[:smaller] equal->nums[smaller:equal] unclassified->[equal:larger] larger->[larger:]
        # At first we assume that all the list is unclassified
        smaller = 0
        equal = 0
        larger = len(nums)
        # iterate through the list up until there is no unclassified element
        while equal < larger:
            if nums[equal] < pivot:
                temp = nums[equal]
                nums[equal] = nums[smaller]
                nums[smaller] = temp
                smaller += 1
                equal += 1
            elif nums[equal] == pivot:
                equal += 1
            else:
                # we need to move it here because it starts from len(nums) and it should be because at first we 
                # assume that all the array is unclassified
                larger -= 1
                temp = nums[equal]
                nums[equal] = nums[larger]
                nums[larger] = temp
                