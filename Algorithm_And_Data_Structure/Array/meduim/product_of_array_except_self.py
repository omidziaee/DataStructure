'''
Created on Jan 23, 2019

@author: USOMZIA
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution():
    def multiplu_except_index(self, nums):
        #Todo: Edge cases
        if len(nums) == 1:
            return nums[0]
        # we need to arrays fo keep the multiplication of before and after the index
        multiply_before_index = [1 for _ in range(len(nums))]
        multiply_after_index = [1 for _ in range(len(nums))]
        result = [0 for _ in range(len(nums))]
        mul_before = 1
        mul_after = 1
        for i in range(1, len(nums)):
            mul_before *= nums[i - 1]
            multiply_before_index[i] = mul_before
        for i in range(len(nums) - 2, -1, -1):
            mul_after *= nums[i + 1]
            multiply_after_index[i] = mul_after
        for i in range(len(nums)):
            result[i] = multiply_before_index[i] * multiply_after_index[i]
        return result
    
sol = Solution()
print sol.multiplu_except_index([1,2,3,4])
