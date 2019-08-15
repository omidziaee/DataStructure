'''
Created on Aug 3, 2019

@author: omid
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward 
k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's
 next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. 
Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and
 backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's
length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, 
but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
'''
class Solution(object):
    def circularArrayLoop_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # This is recursive approach, we need to path the direction, nums, current_index
        if not nums:
            return False
        for i in range(len(nums)):
            direction = nums[i] > 0
            if self.helper(nums, direction, i):
                return True
        return False
            
        
    def helper(self, nums, direction, current_index):
        # base case
        if nums[current_index] == "#":
            return True
        curr_direction = nums[current_index] > 0
        if curr_direction != direction:
            return False
        # The new index after the jump where we end up
        next_index = (current_index + nums[current_index]) % len(nums)
        # This we need it because whatever change we made here should not 
        # reflect to the main nums
        cache = nums[current_index]
        nums[current_index] = "#"
        # loop should not end and start at the same point
        if next_index == current_index:
            res = False
        else:
            res = self.helper(nums, curr_direction, next_index)
        # revert the changes back! Remeber this is in loop recursion and we need 
        # to keep the array without change!
        nums[current_index] = cache
        return res
    
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        for i in range(len(nums)):
            direction = nums[i] > 0
            new_index = (i + nums[i]) % len(nums)
            cache = nums[i]
            nums[i] = "#"
            while True:
                if direction != nums[new_index] > 0:
                    nums[i] = cache
                    break
                if new_index == i:
                    nums[i] = cache
                    break
                if nums[new_index] == "#":
                    return True
                
    
nums = [-1,-2,-3,-4,-5]
sol = Solution()
print sol.circularArrayLoop(nums)
        