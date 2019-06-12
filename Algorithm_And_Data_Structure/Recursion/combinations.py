'''
Created on Jun 2, 2019

@author: omid
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        ans = []
        combination = []
        nums = [num for num in range(1, n + 1)]
        self.to_find_combination(nums, ans, combination, k, 0)
        return ans
    def to_find_combination(self, nums, ans, combination, k, start):
        if len(combination) == k:
            return ans.append(combination)
        for i in range(start, len(nums)):
            if nums[i] in combination:
                continue
            self.to_find_combination(nums, ans, combination + [nums[i]], k, i + 1)
        return ans
