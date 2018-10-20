'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers where 1 a[i] n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    def dispressNum(self, nums):
        nums.sort()
        result = [] 
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                nums.insert(i + 1, nums[i] + 1)
                result.append(nums[i] + 1)
        return result
    
    def disapearedNums(self, nums):
        result = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                result.append(i)
        return result
            
            
            

sol = Solution()
print sol.disapearedNums([1, 1])                
                
            
