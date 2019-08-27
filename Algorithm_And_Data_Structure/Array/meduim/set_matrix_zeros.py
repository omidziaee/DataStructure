'''
Created on Aug 18, 2019

@author: omid
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        As it asks for o(1) space we need to do it in place and manipulate the matrix.
        In all such a problems use the first row and first column elements as flag if there
        is any element in a row or a column is zero. 
        """
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        first_col = False
        # this variable is to an indicator for the first column. for the first row we use matrix[0][0]
        for i in range(rows):
            # Check if any elements in the first column is zero in this case set the first_col to true
            # This is a great idea because this being checked before we change it if any elements on the row is zero
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Now traverse again
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Now check for the first row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        # Now for the first column
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
        
