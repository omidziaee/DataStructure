'''
Created on Aug 20, 2019

@author: USOMZIA
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the 
elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], 
[10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''
class Solution(object):
    def numSubarrayProductLessThanK_rec_all(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = []
        curr_path = []
        self.helper(ans, curr_path, nums, 1, 0, k)
        return ans
    def helper(self, ans, curr_path, nums, mul, start_index, k):
        if mul < k:
            ans.append(curr_path)
        for i in range(start_index, len(nums)):
            self.helper(ans, curr_path + [nums[i]], nums, mul * nums[i], i + 1, k)
        return ans
    
    def numSubarrayProductLessThanK_not_complete(self, nums, k):
        import copy
        mul = 1
        ans = []
        curr = []
        left = 0
        for i in range(len(nums)):
            mul *= nums[i]
            if mul < k:
                curr += [nums[i]]
                ans.append(copy.copy(curr))
            else:
                while mul >= k:
                    mul = mul / nums[left]
                    left += 1
                ans.append(nums[left:i + 1])
                curr = nums[left:i + 1]
        return ans
    
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        mul = 1
        left = ans = 0
        for right, num in enumerate(nums):
            mul *= num
            while mul >= k:
                mul /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
            
    
    
nums = [10, 5, 2, 6] 
k = 100
sol = Solution()
print sol.numSubarrayProductLessThanK(nums, k)
            
