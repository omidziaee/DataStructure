'''
Created on Aug 18, 2019

@author: omid
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that 
A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
'''
class Solution(object):
    def canReorderDoubled_1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True
        A.sort(key=abs)
        dic_count = {} 
        for elem in A:
            if elem in dic_count:
                dic_count[elem] += 1
            else:
                dic_count[elem] = 1
        for elem in A:
            if dic_count[elem] == 0:
                continue
            if 2 * elem not in dic_count or dic_count[2 * elem] == 0:
                return False
            dic_count[elem] -= 1
            dic_count[2 * elem] -= 1
            
        return True
    
    def canReorderDoubled(self, A):
        import collections
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
            
            
A = [1,2,4,16,7,4]
sol = Solution()
print sol.canReorderDoubled_1(A)