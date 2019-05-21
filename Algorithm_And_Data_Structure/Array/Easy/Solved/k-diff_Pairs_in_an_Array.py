'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
'''

class Solution(object):
    # This is not good as it is o(n^2)
    def kDiffNaive(self, nums, k):
        # Integer can be negative
        if k == 0:
            if len(nums) > len(set(nums)):
                return len(nums) - len(set(nums))
            else: 
                return 0
        elif k < 0:
            return 0
        else:
            nums = list(set(nums))
            occurance = 0
            for i in range(len(nums) - 1):
                for j in range(i+1, len(nums)):
                # Here it should be abs as you do not compare a pair twice but for 3 and 5 while k = 2 it needs to be abs
                    if abs(nums[i] - nums[j]) == k:
                        occurance += 1
        return occurance
                
    
    def kDiff(self, nums, k):
        if k == 0:
            # This is wrong [1, 1, 1, 1] and k = 4 the result is wrong
            if len(nums) > len(set(nums)):
                return len(nums) - len(set(nums))
            else:
                return 0
        elif k < 0:
            return 0
        else:
            # Set is similar to dictionary you can not call it by index
            nums = list(set(nums))
            occurance = 0
            for elem in nums:
                if elem - k in nums:
                    occurance += 1
        return occurance
    # This is right
    def kDiffMulOccur(self, nums, k):
        import collections
        dic = collections.defaultdict()
        occurance = 0
        for elem in nums:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
        if k == 0:
            for value in dic.values():
                if value > 1:
                    occurance += 1
        elif k < 0:
            return 0
        else:
            for key in dic:
                if key - k in dic:
                    occurance += 1
        return occurance
            

sol = Solution()
print sol.kDiffMulOccur([1, 1, 1, 2, 2], 0)
