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
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        counter += 1
        return counter
    
    def triangleNumber_does_not_work(self, nums):
        import bisect
        if len(nums) < 3:
            return 0
        counter = 0
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                index = bisect.bisect_right(nums, nums[i] + nums[i - 1])
                while nums[index] == nums[j] and index:
                    index -= 1
                counter += index - j
        return counter
    
    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0
        # Linear scan all the numbers 
        nums.sort()
        counter = 0
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                # Check the first number just if this one is not zero the rest of it won't be zero right?!
                if nums[i] != 0:
                    while k < len(nums) and nums[i] + nums[j] > nums[k]: # check the k here because inside the loop you increase it by one
                        k += 1
                    # minus one because we already did k = j + 1
                    counter += k - j - 1
        return counter
    
    def triangleNumber_3sum(self, nums):
        if len(nums) < 3:
            return 0
        nums.sort()
        counter = 0
        for i in range(len(nums) - 1, 1, -1):
            # So for each inner loop we start scan from begining
            l = 0
            r = i - 1
            while r > l:
                if nums[l] + nums[r] > nums[i]:
                    counter += r - l
                    r -= 1
                else:
                    l += 1
        return counter
                    
    
sol = Solution()
print sol.triangleNumber([48,66,61,46,94,75])