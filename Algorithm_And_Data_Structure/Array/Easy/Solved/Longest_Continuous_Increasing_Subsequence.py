'''
Created on Sep 27, 2018

@author: USOMZIA
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''
class Solution(object):
    def lenLongestIncreasing(self, nums):
        tempMax = 0
        maxLen = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                tempMax += 1
                maxLen = max(maxLen, tempMax)
            else:
                tempMax = 0
        return maxLen + 1
<<<<<<< HEAD
    # Two_pointers
    def lenLongestIncreasing_two_pointers(self, nums):
        # Todo: Edge cases
        right_pointer = 0
        left_pointer = 0
        max_len = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                right_pointer += 1
                
            else:
                max_len = max(max_len, right_pointer - left_pointer + 1)
                right_pointer = i + 1
                left_pointer = i + 1
        # Very Important!! we need to check if the last right pointer is the last element
        if right_pointer == len(nums) - 1:
            max_len = max(max_len, right_pointer - left_pointer + 1)
            
=======
    # ===========================
    # =  Two pointers solution   =
    # ===========================
    def find_max_increasing_length(self, nums):
        # Todo: Edge CASES
        if len(nums) < 2:
            return len(nums)
        # This is a two pointer problem
        left_pointer = 0
        max_len = 0
        for index in range(len(nums)):
            if (index + 1 < len(nums)) and nums[index] >= nums[index + 1]:
                max_len = max(max_len, index - left_pointer + 1)
                left_pointer = index + 1
            if index + 1 == len(nums):
                max_len = max(max_len, index - left_pointer + 1)
                
                
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git
        return max_len
    
sol = Solution()
print sol.lenLongestIncreasing([1, 3, 5, 4, 7, 2])
