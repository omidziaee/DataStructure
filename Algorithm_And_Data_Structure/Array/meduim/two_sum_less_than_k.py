'''
Created on Aug 13, 2019

@author: omid
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
'''
class Solution(object):
    def twoSumLessThanK_ok(self, A, K):
        import bisect
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        max_sum = -float('inf')
        for i, elem in enumerate(A):
            index = bisect.bisect_left(A, K - elem)
            if index > 0:
                if index - 1 != i:
                    max_sum = max(max_sum, elem + A[index - 1])
                else:
                    # This is for the exception if i and index - 1 are equal then we add
                    # the same number twice
                    max_sum = max(max_sum, elem + A[index - 2])
        return max_sum if max_sum != -float('inf') else -1
    def twoSumLessThanK(self, A, K):
        l = 0
        r = len(A) - 1
        A.sort()
        max_sum = -float('inf')
        while l < r:
            if A[l] + A[r] < K:
                max_sum = max(max_sum, A[l] + A[r])
                l += 1
            else:
                r -= 1
        return max_sum if max_sum != -float('inf') else -1
        
                
    
    
# A = [34,23,1,24,75,33,54,8]
# K = 60
A = [358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549]
K = 1800
sol = Solution()
print sol.twoSumLessThanK(A, K)