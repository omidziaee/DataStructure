'''
Created on May 30, 2019

@author: USOMZIA
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) < 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        # Dude binary search should be done on a sorted array
        # So the first step is to find the two sorted subarrays or find the 
        # revert point
        l = 0
        r = len(nums) - 1
        # Kind of divide and conqure to find the change point
        # First we need to check it such a point exist or not
        if nums[l] > nums[r]:
            mid = 0
            while l <= r:
                mid = (l + r) / 2
                # Here we have mid + 1 so for sure we need to create an edge case for the array with the 
                # length equal to one
                if nums[mid] > nums[mid + 1]:
                    # We got it this is the point of change
                    break
                elif nums[mid] > nums[-1]:
                    # the point is the right side as the mid is less than the end
                    l = mid + 1
                elif nums[mid] < nums[0]:
                    r = mid - 1
            # Now we have the index of the change point mid!
            # Check the target is in which side
            if target >= nums[mid + 1] and target <= nums[-1]:
                l = mid + 1
                r = len(nums) - 1
            elif target <= nums[mid] and target >= nums[0]:
                l = 0
                r = mid
        # Now regular binary search
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1
    
sol = Solution()
print sol.search([3,5,1], 1)
                
                