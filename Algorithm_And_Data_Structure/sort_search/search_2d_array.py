'''
Created on Aug 1, 2019

@author: USOMZIA
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution(object):
    def searchMatrix_not_bad(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                if self.binary_search(matrix[i], 0, len(matrix[0]) - 1):
                    return True
        return False
    def binary_search(self,arr, left, right):
        while left <= right:
            mid = (right + left) / 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Beware of edge cases
        if not matrix:
            return False
        # This is how we can convert a 2d array in 1d in memory 
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        # Now if counter of rows equals right // # of columns and counter
        # of columns equals right % # of columns
        while left <= right:
            pivot_indx = (right + left) / 2
            pivot_elem = matrix[pivot_indx / n][pivot_indx % n]
            if target == pivot_elem:
                return True
            else:
                if target < pivot_elem:
                    right = pivot_indx - 1
                else:
                    left = pivot_indx + 1
        return False
        
        
        
    

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 40
sol = Solution()
print sol.searchMatrix(matrix, target)
    