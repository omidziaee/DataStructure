'''
Created on Jan 14, 2019

@author: USOMZIA
'''
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left_pointer = 0
        right_pointer = k
        max_sum = -float('inf')
        while right_pointer <= len(nums):
            sum_k = 0
            for index in range(left_pointer, right_pointer):
                sum_k += nums[index]
            max_sum = max(sum_k, max_sum)
            left_pointer += 1
            right_pointer += 1
        return float(max_sum) / k
    def findMaxAverage_faster(self, nums, k):
        left_pointer = 0
        right_pointer = k - 1 
        sum_k = 0
        max_sum = -float('inf')
        for index in range(k):
            sum_k += nums[index]
        while right_pointer < len(nums):
            max_sum = max(max_sum, sum_k)
            left_pointer += 1
            right_pointer += 1
            if right_pointer < len(nums):
                sum_k = sum_k - nums[left_pointer - 1] + nums[right_pointer]
            
        return float(max_sum) / k
    def findMaxAverage_faster_easier(self, nums, k):
        # You can do better
        # 1) Initialize max_sum with sum_k
        # 2) There is no need to have the pointers
        # The idea is the same as the previous one new sum while we move the window is sum = sum + nums[k] - nums[0] 
        # We know the some the elements from elements i to i + k so from i + 1 to i + k + 1 we just need to add 
        # the i + k + 1 element and subtract the ith element.
        sum_k = 0
        for i in range(k):
            sum_k += nums[i]
        max_k_sum = sum_k
        for j in range(k, len(nums)):
            sum_k += nums[j] - nums[j - k]
            max_k_sum = max(max_k_sum, sum_k)
        return float(max_k_sum) / k
            
            
            

sol = Solution()
nums = [1,12,-5,-6,50,3]
4
print sol.findMaxAverage_faster_easier(nums, 4)