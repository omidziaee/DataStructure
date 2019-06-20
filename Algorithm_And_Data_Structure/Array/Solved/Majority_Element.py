'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
class Solution(object):
    def MajorElem(self, nums):
        import collections
        majorLength = len(nums) / 2
        dic = collections.defaultdict()
        for elem in nums:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
        for key in dic:
            if dic[key] > majorLength:
                return key
        return -1
    
sol = Solution()
print sol.MajorElem([2,2,1,1,1,2,2])
        