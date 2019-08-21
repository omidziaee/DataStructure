'''
Created on Aug 14, 2019

@author: USOMZIA
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented
as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
'''
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j= 0, 0
        combined = []
        while i < len(A) and j < len(B):
            start_A, end_A = A[i]
            start_B, end_B = B[j]
            lo = max(start_A, start_B)
            hi = min(end_A, end_B)
            if lo <= hi:
                combined.append([lo, hi])
            # remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
            
        return combined
                
                
                
        
                
    
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
# A = [[14,16]]
# B = [[7,13],[16,20]]
sol = Solution()
print sol.intervalIntersection(A, B)
                