'''
Created on Sep 27, 2018

@author: USOMZIA
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''
class Solution(object):
    def findArrDegree(self, nums):
        import collections
        dPos = collections.defaultdict()
        dOccur = collections.defaultdict()
        maxFrequent = 0
        result = 1e10
        for i, elem in enumerate(nums):
            if elem in dPos:
                dPos[elem].append(i)
                dOccur[elem] += 1
            else:
                dPos[elem] = [i]
                dOccur[elem] = 1
        for key in dOccur:
            if dOccur[key] >= maxFrequent:
                maxFrequent = dOccur[key]
        maxKeys = [key for key, value in dOccur.items() if value == maxFrequent]
        for key in maxKeys:
            if max(dPos[key]) - min(dPos[key]) + 1 < result:
                result = max(dPos[key]) - min(dPos[key]) + 1
        return result
    
sol = Solution()
print sol.findArrDegree([1, 2, 2, 3, 1])
                
            
                   
        
        
        