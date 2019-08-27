'''
Created on Jan 23, 2019

@author: USOMZIA
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.          
'''
class Solution(object):
    def pancakeSort(self, A):
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    # After each f flip the element at place i will move to f + 1 - i
                    # [4, 2, 3, 1] after 4 flip -> [1, 3, 2, 4] so 3 was at index 3 (1 start
                    # not 0). Now after 4 flip it goes to 4 + 1 - 3 = 2
                    i = f+1 - i
            ans.extend([i, N])
            # The last placement should decrease by one after each iteration
            N -= 1

        return ans
    
A = [3,2,4,1]
sol = Solution()
print sol.pancakeSort(A)