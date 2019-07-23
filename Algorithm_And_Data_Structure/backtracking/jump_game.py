'''
Created on Jul 11, 2019

@author: omid
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start_index = 0
        return self.helper(nums, start_index)
    def helper(self, nums, start_index):
        # base case
        if start_index == len(nums):
            return True
        max_position = min(start_index + nums[start_index], len(nums) - 1)
        for position in range(start_index + 1, max_position + 1):
            if self.helper(nums, position):
                return True
        return False
    
sol = Solution()
nums = [2,3,1,1,4]
print sol.canJump(nums)
                