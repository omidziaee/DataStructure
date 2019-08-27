'''
Created on Aug 20, 2019

@author: USOMZIA
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  
Return -1 if no such i exists.

Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation: 
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
Example 2:

Input: [0,2,5,8,17]
Output: 0
Explanation: 
A[0] = 0, thus the output is 0.
Example 3:

Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: 
There is no such i that A[i] = i, thus the output is -1.
'''
class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        ans = float('inf')
        while l <= r:
            mid = l + (r - l) / 2
            target = A[mid]
            if target == mid:
                ans = mid
                # you are not sure if the first one found is the minimum search lesser values
                r = mid - 1
            elif target < mid:
                l = mid + 1
            elif target > mid:
                r = mid - 1
        return ans if ans != float("inf") else -1
    def fixedPoint_easy(self, A):
        for i, elem in enumerate(A):
            if i == elem:
                return i
        return -1