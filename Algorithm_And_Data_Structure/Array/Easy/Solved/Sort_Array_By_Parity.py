'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
'''
class Solution(object):
    def SortParity(self, nums):
        odds = []
        evens = []
        for elem in nums:
            if elem % 2 == 0:
                evens.append(elem)
            else:
                odds.append(elem)
        return evens + odds
    
sol = Solution()
print sol.SortParity([3,1,2,4])