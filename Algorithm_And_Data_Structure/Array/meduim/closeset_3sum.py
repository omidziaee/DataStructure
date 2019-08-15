'''
Created on Aug 14, 2019

@author: USOMZIA
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers.
 You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        nums.sort()
        max_sum = float('inf')
        for i in range(len(nums) - 2):
            # pass the same elements
            # This means we did the same for the previous one no need to repeat it again
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r] 
                if s < target:
                    # This make it faster
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                elif s > target:
                    # This make it faster
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                else:
                    return s
                # Now compare the distance of current sum to the target and the max_sum with the target.
                if abs(s - target) < abs(max_sum - target):
                    max_sum = s
        return max_sum

nums = [-1, 2, 1, -4]    
target = 1
sol = Solution()
print sol.threeSumClosest(nums, target)