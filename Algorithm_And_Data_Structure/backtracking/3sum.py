'''
Created on Jun 12, 2019

@author: USOMZIA
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum_general(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return [] 
        nums.sort()
        target = 0
        ans = []
        path = []
        self.to_find_all_paths(nums, ans, path, target, 0)
        return ans
    def to_find_all_paths(self, nums, ans, path, target, start_index):
        if target == 0 and len(path) == 3:
            return ans.append(path)
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            if target + nums[i] > 0 or len(path) > 3:
                break
            else:
                self.to_find_all_paths(nums, ans, path + [nums[i]], target + nums[i], i + 1)
        return ans
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        l = 0
        r = len(nums) - 1
        i = 0
        res = []
        while (l <= r) and i < len(nums):
            if (nums[l] + nums[i] + nums[r]) > 0:
                r -= 1
            elif (nums[l] + nums[i] + nums[r]) < 0:
                l += 1
            else:
                res.append([nums[l], nums[r], nums[i]])
            i += 1
            l += 1
            r -= 1
        return res
            
                
            
        
    
    
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print sol.threeSum(nums)