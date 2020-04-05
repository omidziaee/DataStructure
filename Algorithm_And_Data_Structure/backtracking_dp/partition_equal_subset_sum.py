'''
Created on Oct 10, 2019

@author: omid
Given a non-empty array containing only positive integers, find if the array can be partitioned into two 
subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        nums.sort()
        sum_total = sum(nums)
        if sum_total % 2 != 0:
            return False
        return self.dfs(nums, sum_total / 2, 0)
    def dfs(self, nums, target, start):
        if target == 0:
            return True
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if target >= 0:
                if self.dfs(nums, target - nums[i], i + 1):
                    return True
        return False