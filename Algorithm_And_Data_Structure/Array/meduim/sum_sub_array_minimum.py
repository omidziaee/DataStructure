'''
Created on Aug 11, 2019

@author: omid
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
'''
class Solution():
    def find_subsets(self, A):
        # Move from each element to the left and right and find the first previous less number and first
        # next less number
        res = 0
        stack = []  #  non-decreasing 
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1]) 
            stack.append(i)
        return res % (10**9 + 7)
    
    def sumSubarrayMins(self, A):
        stack_p = []
        stack_n = []
        # Initialize
        left, right = [], []
        for i in range(len(A)):
            left.append(i + 1)
        for i in range(len(A)):
            right.append(len(A) - i)
        for i in range(len(A)):
            while (stack_p and A[stack_p[-1]] > A[i]):
                stack_p.pop()
            left[i] = i + 1 if not stack_p else i - stack_p[-1]
            stack_p.append(i)
            while (stack_n and A[stack_n[-1]] > A[i]):
                x = stack_n.pop()
                right[x] = i - x
            stack_n.append(i)
        ans, mod = 0, 1e9+7
        for i in range(len(A)):
            ans = (ans + A[i] * left[i] * right[i]) % mod
        return ans
    
nums = [3, 1, 2, 4]
sol = Solution()
print sol.sumSubarrayMins(nums)
                
        

