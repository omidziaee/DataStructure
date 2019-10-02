'''
Created on Oct 2, 2019

@author: omid
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum 
array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Intuition

We can make the following logical steps to arrive at the solution:

As we only care about whether each element is less than, between, or greater than the interval [L, R], let's pretend 
each element is either 0 if it is less than L; 1 if it is between L and R; or 2 if it is greater than R.

Then, we want the number of subarrays with no 2 and at least one 1. The 2s split the array into groups of arrays with 
only 0s and 1s. For example, if our array is [0, 0, 1, 2, 2, 1, 0, 2, 0], then the answer is just the 
answer for [0, 0, 1] plus the answer for [1, 0] plus the answer for [0].

For each such group (arrays of only 0s or 1s), to count the number of subarrays that have at least one 1, let's count all 
the subarrays in the group, minus the subarrays that only have zeroes.

For example, [0, 0, 1] has 6 subarrays, 3 of which are zero-only, which adds 3 to the answer; [1, 0] has 3 subarrays, 1 
of which is zero-only, which adds 2 to the answer; and [0] has 1 subarray, 1 of which is zero-only, which adds 0 to the 
answer. The final answer to the previous original example of A = [0, 0, 1, 2, 2, 1, 0, 2, 0] is 3 + 2 + 0 = 5.

Algorithm

Say count(B) is the number of subarrays that have all elements less than or equal to B. From the above reasoning, the 
answer is count(R) - count(L-1).

How do we compute count(B)? We remember cur, the number of contiguous, previous elements less than or equal to B. When 
we see a new element less than or equal to B, the number of valid subarrays ending at this position is cur + 1. When 
we see a new element greater than B, the number of valid subarrays ending at this position is 0.
'''
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.count(A, R) - self.count(A, L - 1)
    def count(self, A, num):
        counter = ans = 0 
        for i in range(len(A)):
            if A[i] <= num:
                counter += 1
                ans += counter
            else:
                counter = 0
        return ans