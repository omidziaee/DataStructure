'''
Created on Apr 5, 2019

@author: omid
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # first transpose the matrix
        cols = len(matrix[0])
        rows = len(matrix)
        for i in range(rows):
            # Transpose in place needs this starts from i
            # If there is a new matrix both loops can start
            # from zero
            for j in range(i, cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # now reverse each row
        for k in range(rows):
            start = 0
            end = cols - 1
            self.reverse(matrix[k], start, end)
        return matrix
    def reverse(self, row, start, end):
        while start < end:
            temp = row[start]
            row[start] = row[end]
            row[end] = temp
            start += 1
            end -= 1
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]       
sol = Solution()
print sol.rotate(matrix)
