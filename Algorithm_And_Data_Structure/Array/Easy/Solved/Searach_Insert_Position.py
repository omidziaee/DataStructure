'''
Created on Sep 24, 2018

@author: USOMZIA
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 2:
            return False
        mid = len(nums) / 2
        leftSide = nums[:mid]
        rightSide = nums[mid + 1:]
        if target < nums[mid]:
            return self.searchInsert(leftSide, target)
        elif target > nums[mid]:
            return self.searchInsert(rightSide, target)
        elif target == nums[mid]:
            return mid
        
    def funcFind(self, nums, target):
        if nums[-1] < target:
            return len(nums)
        for i, elem in enumerate(nums):
            if elem < target:
                continue
            elif elem > target:
                result = i if i >= 1 else 0
                return result
            elif elem == target:
                return i
            
    def smartFind(self, nums, target):
        return len([x for x in nums if x < target])
    
    def binSearch(self, nums, target):
        right = len(nums) - 1
        left = 0
        
        while left <= right:
            mid = (right + left) / 2
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return left
            
            
        
sol = Solution()
print sol.binSearch([1, 3, 5, 6], 7)