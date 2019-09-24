'''
Created on Sep 22, 2019

@author: omid
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
'''
class Solution(object):
    def partitionDisjoint_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # this is o(n^2) and brute-force
        if len(A) < 2:
            return -1
        for i in range(1, len(A) - 1):
            if self.is_midpoint(A, i):
                return i
        return -1
    def is_midpoint(self, A, i):
        for j in range(0, i):
            for k in range(i, len(A)):
                if A[j] > A[k]:
                    return False
        return True
    
    def partitionDisjoint(self, A):
        # Instead of finding two subarrays with all the left elements less than all the right elements
        # lets find two subarrays that max of the left is less than min of the right side
        n = len(A)
        min_sofar = [float('inf') for _ in range(n)]
        max_sofar = [-float('inf') for _ in range(n)]
        m = -float('inf')
        for i in range(n):
            m = max(m, A[i])
            max_sofar[i] = m
        m = float('inf')
        for i in range(n - 1, -1, -1):
            m = min(m, A[i])
            min_sofar[i] = m
        for i in range(1, n):
            if max_sofar[i - 1] <= min_sofar[i]:
                return i
        return -1
            
            
            
with open("input.csv", "r") as f:
    data = list(f.read().split(","))        
ans = []
for i in range(len(data)):
    ans.append(int(data[i]))
import time
start = time.time()
sol = Solution()
print sol.partitionDisjoint(ans)
print time.time() - start
                
        