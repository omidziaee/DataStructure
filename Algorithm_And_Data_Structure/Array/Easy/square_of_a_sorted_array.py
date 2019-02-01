'''
Created on Jan 23, 2019

@author: USOMZIA
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
class Solution():
    # This is o(nlgn)
    def sortedSquares_easy(self, A):
        for i in range(len(A)):
            A[i] = A[i]**2
        # return sorted([num ** 2 for num in A]) 
        return sorted(A)
    
    # This is two pointers and it is o(n)
    def sortedSquares(self, A):
        # if all the numbers are positive we do not need to do anything otherwise
        # we need to divide the array to the negative and positive section then square 
        # each section. The merge the two sorted sub lists. Just bear in mind that for
        # the negative section you need to do it in reverse. [-3, -2, -1] --> [9, 4, 1]
        # Find the index of the first positve number
        # i for the positive numbers and j for the negative numbers
        # this is o(n) where n in the length of A
        j = 0
        i = 0
        while j < len(A) and A[j] < 0:
            j += 1
        # now set the index of the last negative bear in mind [-3, -2, -1, 1, 2, 3] j will be 3!
        i = j
        j = j - 1
        result = []
        while i < len(A) and j >= 0:
            if A[i] ** 2 < A[j] ** 2:
                result.append(A[i] ** 2)
                i += 1
            elif A[j] ** 2 <= A[i] ** 2:
                result.append(A[j] ** 2)
                j -= 1
        while i < len(A):
            result.append(A[i] ** 2)
            i += 1
        while j > 0:
            result.append(A[j] ** 2)
            j -= 1
        return result
            
        
    
sol = Solution()
print sol.sortedSquares([-7,-3,2,3,11])
