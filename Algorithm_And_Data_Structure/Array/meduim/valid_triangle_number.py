'''
Created on Sep 24, 2019

@author: USOMZIA
Given an array consists of non-negative integers, your task is to count the number 
of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
'''
class Solution():
    def triangleNumber_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case
        if len(nums) < 3:
            return 0
        counter = 0
        # Choose all the 3plets and check if they satisfy the constraint
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] < nums[k] and nums[i] + nums[k] < nums[j] and nums[j] + nums[k] < nums[i]:
                        counter += 1
        return counter
    
    def triangleNumber(self, nums):
        import bisect
        if len(nums) < 3:
            return 0
        counter = 0
        nums.sort()
        for i in range(2, len(nums)):
            index = bisect.bisect_right(nums, nums[i] + nums[i - 1])
            if len(nums) > index and index > 0 and nums[index] != nums[index - 1]:
                counter += 1
        return counter
    
sol = Solution()
print sol.triangleNumber([2, 3, 2, 4])