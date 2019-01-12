'''
Created on Jan 11, 2019

@author: USOMZIA
'''
class Solution():
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is recursive
        # base case 
        if len(nums) == 0:
            return 0
        if 0 < len(nums) <= 2:
            return max(nums)
        keep_max_rub = [0 for _ in range(len(nums))]
        for index in range(len(nums)):
            keep_max_rub[index] = nums[index] + self.rob(nums[index + 2:])
            
        return max(keep_max_rub)
    
    
    
    
    
    
    
    
    
    
    
    
    
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
sol = Solution()
print sol.rob(nums)