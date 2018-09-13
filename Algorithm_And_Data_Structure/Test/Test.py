'''
Created on Sep 5, 2018

@author: USOMZIA
'''
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
sol = Solution()
print sol.twoSum([1, 2, 3, 5], 4)