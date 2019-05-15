'''
Created on May 14, 2019

@author: USOMZIA
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search 
target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        # It should be less than or equal to to be able to handle the one element array [5] and target is 5
        while left <= right:
            mid = (right + left) / 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
        return -1
    def search_bin(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bin_search(nums, target, len(nums) - 1, 0)
    def bin_search(self, nums, target, r, l):
        if r < l:
            return -1
        mid = (r + l) / 2
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < target:
                l = mid + 1
                return self.bin_search(nums, target, r, l)
            else:
                r = mid - 1
                return self.bin_search(nums, target, r, l)