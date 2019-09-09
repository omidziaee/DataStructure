'''
Created on Sep 4, 2019

@author: USOMZIA
Suppose an array sorted in ascending order is rotated at some 
pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) < 3:
            return min(nums)
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[l]:
            return nums[l]
        while l <= r:
            if r - l <= 1:
                return min(nums[l], nums[r])
            mid = l + (r - l) / 2
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return nums[mid + 1]
                elif nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                    return nums[mid]
                elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    if nums[mid] > nums[r]:
                        l = mid + 1
                    elif nums[mid] < nums[r]:
                        r = mid - 1
                # The case that nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1] never will happen
        return -1
        
        
sol = Solution()
print sol.findMin([1, 2, 3, 4, 5])