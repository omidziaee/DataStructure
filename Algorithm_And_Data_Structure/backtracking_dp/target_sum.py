'''
Created on Jul 1, 2019

@author: USOMZIA
'''
# For path it is not easy to have memoization but for count it is easy
class Solution(object):
    def __init__(self):
        self.count = 0
        self.memo = {}
    def findTargetSumWays_path(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        ans = []
        current_path = []
        self.helper_path(nums, S, ans, current_path, 0, 0)
        return ans
    def helper_path(self, nums, target, ans, curr_path, start_index, sum_num):
        if start_index == len(nums):
            if sum_num == target:
                return ans.append(curr_path)
            else: 
                return []
        # There is no need for a loop as we dont want the permutations starts from the middle we need 
        # whatever from the start
        self.helper_path(nums, target, ans, curr_path + [nums[start_index]], start_index + 1, sum_num + nums[start_index])
        self.helper_path(nums, target, ans, curr_path + [-nums[start_index]], start_index + 1, sum_num - nums[start_index])
        return ans
    
    
    def findTargetSumWays(self, nums, S):
        return self.helper(nums, S, 0, 0)
    def helper(self, nums, target, start_index, sum_num):
        if start_index == len(nums):
            if target == sum_num:
                return 1
            else:
                return 0
        if (start_index, sum_num) in self.memo:
            return self.memo[(start_index, sum_num)]
        add = self.helper(nums, target, start_index + 1, sum_num + nums[start_index])
        minus = self.helper(nums, target, start_index + 1, sum_num - nums[start_index])
        self.memo[(start_index, sum_num)] = add + minus
        return add + minus
        
        
    
    
sol = Solution()
print sol.findTargetSumWays_path([1,1,1,1,1],3)