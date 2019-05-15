'''
Created on Jan 8, 2019

@author: USOMZIA
'''
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        number_of_rows = len(A)
        number_of_columns = len(A[0])
        # Use list comprehension
        # Never use A_transpose = [[None] * number_of_columns] * number_of_rows this is WRONG
        # it acually copies each row and its values to the number_of_rows times
        # Always use list comprehension to create new lists and initialze them
        A_transpose = [[None for _ in range(number_of_rows)] for _ in range(number_of_columns)]
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                A_transpose[column_index][row_index] = A[row_index][column_index]
        return A_transpose
                
                
sol = Solution()
A = [[1,2,3],[4,5,6]]
print sol.transpose(A)