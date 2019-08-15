'''
Created on Aug 3, 2019

@author: omid
'''
class Solution(object):
    #=======================================================================
    def fourSum_works_but_TLE(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # recursive
        if not nums and target == 0:
            return []
        nums.sort()
        ans = []
        curr_path = []
        self.helper(nums, ans, curr_path, target, 0)
        return ans
    def helper(self, nums, ans, curr_path, target, start_index):
        if len(curr_path) == 4 and target == 0:
            ans.append(curr_path)
        for i in range(start_index, len(nums)):
            #if target < nums[i] * 4 or target > nums[-1] * 4:  # take advantages of sorted list
            #    continue
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            self.helper(nums, ans, curr_path + [nums[i]], target - nums[i], i + 1)
        return ans
    #=========================================================================
    
    
    
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
sol = Solution()
print sol.fourSum(nums, target)