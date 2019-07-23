'''
Created on Jul 11, 2019

@author: USOMZIA
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
    def __init__(self):
        self.memo = {}
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
#         if 0 not in nums:
#             return True
        start_index = 0
        return self.helper(nums, start_index)
    def helper(self, nums, start_index):
        if start_index == len(nums) - 1:
            return True
        if start_index in self.memo:
            return self.memo[start_index] == 1
        else:
            max_jump = min(nums[start_index] + start_index, len(nums) - 1)
            for next_position in range(start_index + 1, max_jump + 1):
                if self.helper(nums, next_position):
                    self.memo[start_index] = 1
                    return True
        self.memo[start_index] = 0
        return False
    def canJump_works(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 not in nums:
            return True
        # we set the goal to the last elem if from each index we could jump to the goal then 
        # the new goal would be current index ans so on so force.
        # At first goal is to reach the last element. then from the previous one if it is not 
        # zero of course we can reach to the last. So goal is set the one before the last ...
        goal = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
sol = Solution()
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print sol.canJump(nums)