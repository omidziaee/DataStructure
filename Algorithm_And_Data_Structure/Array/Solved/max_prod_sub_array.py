'''
Created on Jul 9, 2019

@author: omid
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is similar to what we do for max sum but here it is not right to restart 
        # when we get to a positive number if the past sums is negative because maybe the multiplication 
        # is so far negative then a positive number comes if we restart the result and then another negative number comes in our assumption is going to be wrong. Therefore, we need to take 
        # care of this with another variable that keeps minimum values so far as well.
        big = small = max_mul = nums[0]
        for i in range(1, len(nums)):
            # big and small here should come from the previous round of calculation
            # They are actually big and small so far!!
            l_big = max(small * nums[i], big * nums[i], nums[i])
            l_small = min(small * nums[i], big * nums[i], nums[i])
            big = l_big
            small = l_small
            max_mul = max(max_mul, big)
        return max_mul
                
        
        
    
sol = Solution()
print sol.maxProduct([-4, -3, -2])