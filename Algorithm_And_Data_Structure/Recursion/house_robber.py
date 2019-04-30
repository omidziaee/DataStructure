'''
Created on Apr 19, 2019

@author: USOMZIA
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
Best solution:
    https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
    There is some frustration when people publish their perfect fine-grained algorithms without sharing any information abut how they were derived. This is an attempt to change the situation. There is not much more explanation but it's rather an example of higher level improvements. Converting a solution to the next step shouldn't be as hard as attempting to come up with perfect algorithm at first attempt.

This particular problem and most of others can be approached using the following sequence:

Find recursive relation
Recursive (top-down)
Recursive + memo (top-down)
Iterative + memo (bottom-up)
Iterative + N variables (bottom-up)
Step 1. Figure out recursive relation.
A robber has 2 options: a) rob current house i; b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
So it boils down to calculating what is more profitable:

robbery of current house + loot from houses before the previous
loot from the previous house robbery and any loot captured before that
rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is recursive
        # base case
        # it is much better to send the last element first
        # at each state f(i) = max(f(i - 1), f(i - 2) + nums[i]) 
        i = 0
        memo = {}
        return self.rob_helper(nums, i, memo)
    def rob_helper(self, nums, i, memo):
        # This is important as we have nums[i] at the end of the first_part 
        # i can not be greater than len(nums) in this case after the first return as the 
        # value of i is 2 more than the length of the array nums[len(nums)] would create 
        # a problem and it is not correct
        if i > len(nums) - 1:
            return 0
        if i in memo:
            return memo[i]
        first_part = self.rob_helper(nums, i + 2, memo) + nums[i]
        second_part = self.rob_helper(nums, i + 1, memo)
        result = max(first_part, second_part)
        memo[i] = result
        return result
    
    # same as previous one just start from the end which makes more sense
    def rob_2(self, nums):
        # hear we start from the end of the list
        i = len(nums) - 1
        memo = {}
        return self.rob_helper_2(i, nums, memo)
    def rob_helper_2(self, i, nums, memo):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        result = max(self.rob_helper_2(i - 2, nums, memo) + nums[i], self.rob_helper_2(i - 1, nums, memo))
        memo[i] = result
        return result
        
    def dp_rob(self, nums):
        # rob[i] = max(rob[i - 1], nums[i] + rob[i - 2])
        if len(nums) <= 2:
            # for the empty list we can not run the max function
            if not nums:
                return 0
            return max(nums)
        rob = [0 for _ in range(len(nums))]
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob[i] = max(rob[i - 1], nums[i] + rob[i - 2])
        return rob[-1]      
    
    def dp_rob_2(self, nums):
        # This is another dp as it can be seen in the previous solution instead of the array we just 
        # need two variables to keep the value of the prev and prev_prev max and then as we go we can
        # swap these two values.  
        if len(nums) <= 2:
            if not nums:
                return 0
            return max(nums)
        prev_max_state = nums[0]
        curr_max_state = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = curr_max_state
            curr_max_state = max(prev_max_state + nums[i], curr_max_state)
            prev_max_state = temp
        return curr_max_state
        
    
sol = Solution()
print sol.dp_rob_2([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])