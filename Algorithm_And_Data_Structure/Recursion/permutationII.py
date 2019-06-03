'''
Created on Jun 2, 2019

@author: omid
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        perms = []
        used = [False for _ in range(len(nums))]
        self.to_find_all_perms(nums, ans, perms, used)
        return ans
    def to_find_all_perms(self, nums, ans, perms, used):
        if len(perms) == len(nums):
            return ans.append(perms)
        for i in range(len(nums)):
            # Check if it has been used or the current and the previous is the same
            # and the previous one has been used
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i - 1]):
                continue
            used[i] = True
            self.to_find_all_perms(nums, ans, perms + [nums[i]], used)
            # For the past perm it is used but for the new one it can be used again
            used[i] = False
        return ans