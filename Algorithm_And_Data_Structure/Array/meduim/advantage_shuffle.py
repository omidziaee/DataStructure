'''
Created on Sep 3, 2019

@author: USOMZIA
Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32,24], B = [13,25,32,11,11]
Output: [24,32,8,12]
'''
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # sort the first array and find the place of second array elements in the first one
        # with bisect but it should be bisect_right!!
        import bisect
        ans = []
        A.sort()
        for num in B:
            indx = bisect.bisect_right(A, num)
            if indx == len(A):
                ans.append(A.pop(0))
            else:
                ans.append(A.pop(indx))
        return ans
    
A = [2,0,4,1,2]
B = [1,3,0,0,2]
sol = Solution()
print sol.advantageCount(A, B)