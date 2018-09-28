'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
My Solution: First sort the array and then take the last two pairs and run the function on it
'''

class Solution(object):
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        
        mid = len(arr) / 2
        leftSide = self.mergeSort(arr[:mid])
        rightSide = self.mergeSort(arr[mid:])
        
        i = 0
        j = 0
        k = 0
        
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                arr[k] = leftSide[i]
                i += 1
            else:
                arr[k] = rightSide[j]
                j += 1
            k += 1
            
        while i < len(leftSide):
            arr[k] = leftSide[i]
            i += 1
            k += 1
            
        while j < len(rightSide):
            arr[k] = rightSide[j]
            j += 1
            k += 1
        return arr
    
    def takeLastTwo(self, arr):
        result = self.mergeSort(arr)
        sumLastTwo = result[-2] + result[-4]
        return sumLastTwo
        
        
        
sol = Solution()
print sol.takeLastTwo([2,4,112,6,300,400])
