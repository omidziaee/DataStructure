'''
Created on May 18, 2019

@author: omid
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
'''
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a_num = 0
        x = len(A) - 1
        res = []
        carry_over = 0
        for i in range(len(A) - 1, -1, -1):
            a = K % 10
            sum_num = A[i] + a + carry_over
            if sum_num > 9:
                carry_over = sum_num / 10
                sum_num %= 10
            else:
                carry_over = 0
            res.insert(0, sum_num)
            K /= 10 #143/10 -> 14
        K += carry_over # for the last carry_over
        while K > 0: # if K is greater than A
            res.insert(0, K % 10)
            K /= 10
        return res