'''
Created on Feb 6, 2019

@author: USOMZIA
input the row number and output is the values on that column
Example input is 3 output is [1, 3, 3, 1]
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        pascal_array = []
        pascal_array.append([1])
        for j in range(1, rowIndex + 1):
            inner_array = [None for _ in range(j + 1)]
            inner_array[0], inner_array[-1] = 1, 1
            for k in range(1, len(inner_array) - 1):
                inner_array[k] = pascal_array[j - 1][k - 1] + pascal_array[j - 1][k]
            pascal_array.append(inner_array)
            
        return pascal_array[rowIndex]
    
    def get_row(self, rowIndex):
        if rowIndex == 0:
            return [1]
        A = self.get_row(rowIndex - 1)
        new_col = [1] + [A[i] + A[i + 1] for i in range(len(A) - 1)] + [1]
        return new_col
 
                
sol = Solution()
print sol.get_row(3)
