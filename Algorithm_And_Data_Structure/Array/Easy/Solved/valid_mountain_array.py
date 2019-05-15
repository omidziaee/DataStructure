'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
Created on Jan 16, 2019

@author: omid
'''
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Point is to use while and the and to compare then when you say
        # A[i + 1] it means i + 1 <= len(A) - 1
        i = 0
        # First we need to find the peak
        while i + 1 <= len(A) - 1 and A[i + 1] > A[i]:
            i += 1
        # Peak can not be first or last element
        if i == 0 or i == len(A) - 1:
            return False
        # Now we move downward and moving forward the pointer.
        while i+1 <= len(A) - 1 and A[i + 1] < A[i]:
            i += 1
        # At the end, if the pointer arrives to the last element then we are good
        return i == len(A) - 1
