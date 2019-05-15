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
    def permute(self, nums):
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
    
    
sol = Solution()
print sol.permute([1, 2, 3])
                
