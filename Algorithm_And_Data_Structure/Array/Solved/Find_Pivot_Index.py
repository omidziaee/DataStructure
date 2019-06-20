'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
'''
class Solution():
    # This is wrong!!!!
    def find_the_pivot_index(self, nums):
        floor = 0
        ceiling = len(nums)
        half_index = (floor + ceiling) / 2
        while (half_index > floor and (half_index + 1 < ceiling)):
            sum_right_half = 0
            sum_left_half = 0
            for i in range(half_index):
                sum_left_half += nums[i]
            for j in range(half_index + 1, len(nums)):
                sum_right_half += nums[j]
            if sum_right_half == sum_left_half:
                return half_index
            if sum_right_half > sum_left_half:
                half_index += 1
            else:
                half_index -= 1
        return -1
    def find_prior_and_after(self, nums):
        # This is like the multiplication of after and after the index
        sum_before_index = [0 for _ in range(len(nums))]
        sum_after_index = [0 for _ in range(len(nums))]
        
        for before_index in range(1, len(nums)):
            sum_before_index[before_index] = sum_before_index[before_index - 1] + nums[before_index - 1]
        # The last one should be zero that is the reason why it starts at -2
        for after_index in range(len(nums) - 2, -1, -1):
            sum_after_index[after_index] = sum_after_index[after_index + 1] + nums[after_index + 1]
        for index in range(len(nums)):
            if sum_before_index[index] == sum_after_index[index]:
                return index
        return -1
    # The following is also good
    def find_pivot_index(self, nums):
        # Todo: Edge cases
        if len(nums) < 3:
            raise Exception("The length of the array should be greatar than 2!")
        # Initialze
        sum_before_index = [0 for _ in range(len(nums))]
        sum_after_index = [0 for _ in range(len(nums))]
        sum = 0
        for index in range(1, len(nums)):
            sum += nums[index - 1]
            sum_before_index[index] = sum
        sum = 0
        for index in range(len(nums) - 2, -1, -1):
            sum += nums[index + 1]
            sum_after_index[index] = sum
        for index in range(len(sum_before_index)):
            if sum_before_index[index] == sum_after_index[index]:
                return index
        return -1
    
sol = Solution()
print sol.find_pivot_index([1, 7, 3, 6, 5, 6])
