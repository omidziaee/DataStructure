'''
Created on Feb 12, 2019

@author: USOMZIA
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute_old(self, nums):
        # This is recursive problem
        # base case
        if len(nums) == 1:
            # It is essential to put it in bracket because otherwise when it is one you can  not
            # concatinate it to the num_in_i
            return [nums]
        permutations = []
        for i in range(len(nums)):
            num_in_i = nums[i]
            rest_perm = self.permute(nums[:i] + nums[i + 1:])
            for perm in rest_perm:
                permutations.append([num_in_i] + perm)
                    
        return permutations
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        combination = []
        self.to_find_all_perm(nums, ans, combination)
        return ans
    def to_find_all_perm(self, nums, ans, combination):
        if len(combination) == len(nums):
            ans.append(combination)
        for i in range(len(nums)):
            if nums[i] in combination:
                continue
            self.to_find_all_perm(nums, ans, combination + [nums[i]])
        return ans
    
    
sol = Solution()
print sol.permute([1, 2, 3])
                
