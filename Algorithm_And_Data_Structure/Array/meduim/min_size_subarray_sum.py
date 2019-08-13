'''
Created on Aug 12, 2019

@author: USOMZIA
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s.
 If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
# Note: if it askef for equal sum we could use dictionary!!
class Solution(object):
    def minSubArrayLen_ontwo(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        for i in range(len(nums)):
            sum_temp = 0
            for j in range(i, len(nums)):
                sum_temp += nums[j]
                if sum_temp >= s:
                    min_length = min(min_length, j - i + 1)
                    break
        return min_length if min_length != float('inf') else 0
    def minSubArrayLen(self, s, nums):
        min_length = float('inf')
        left = 0
        sum_temp = 0
        for i in range(len(nums)):
            sum_temp += nums[i]
            # So we need to check if we remove from the left of subarray can we still get the same result
            while sum_temp >= s:
                min_length = min(min_length, i - left + 1)
                # Now we need to move forward the left pointer to the right place
                sum_temp -= nums[left]
                left += 1
        return min_length
        
    
s = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print sol.minSubArrayLen(s, nums)