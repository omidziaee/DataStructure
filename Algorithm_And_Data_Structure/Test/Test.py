'''
Created on Sep 5, 2018

@author: USOMZIA
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for key in range(len(nums)):
            if nums[key] in d:
                return [d[key], key]
            else:
                d[target - nums[key]] = key
                    
sol = Solution()                   
Temp = sol.twoSum([2,7,11,15], 9)