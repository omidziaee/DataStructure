'''
Created on Feb 7, 2019

@author: USOMZIA
'''
class Solution(object):
    # This is the driver function the input is a number of rows
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal_matrix = [ [None] * i for i in range(1, rowIndex + 1)]
        return self.helper_function(pascal_matrix, 0)
    def helper_function(self, pascal_matrix, row):
        # base_case
        if row >= len(pascal_matrix):
            return pascal_matrix
        for col in range(len(pascal_matrix[row])):
            if col == row or col == 0:
                pascal_matrix[row][col] = 1
            else:
                pascal_matrix[row][col] = pascal_matrix[row - 1][col - 1] + pascal_matrix[row - 1][col]
                
        return self.helper_function(pascal_matrix, row + 1)

        
        
        
 
                
sol = Solution()
print sol.getRow(5)