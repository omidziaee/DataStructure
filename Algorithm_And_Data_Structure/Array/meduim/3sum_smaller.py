'''
Created on Aug 19, 2019

@author: USOMZIA
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.
Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
'''
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        #res = []
        sum_num = 0
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s >= target:
                    r -= 1
                if s < target:
                    # all the numbers between l and r including l and r satisfy the constraint
                    for k in range(1, r - l + 1):
                        #res.append([nums[i], nums[l], nums[l + k]])
                        sum_num += 1
                    l += 1
        return sum_num
                    
                    
    
nums = [-1,1,-1,-1]
target = -1
sol = Solution()
print sol.threeSumSmaller(nums, target)