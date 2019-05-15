'''
Created on Apr 22, 2019

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
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            head = [nums[i]]
            tail = nums[:i] + nums[i + 1:]
            tails_permute = self.permute(tail)
            for tail_permute in tails_permute:
                res.append(head + tail_permute)
        return res
    
sol = Solution()
print sol.permute([1, 2, 3])