'''
Created on Jan 30, 2020

@author: omidziaee
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then 
return the sorted array.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
'''
class Solution():
    def sort_diagonal(self, mat):
        if not mat:
            return None
        row, col = len(mat), len(mat[0])
        d = {}
        for i in range(row):
            for j in range(col):
                if i - j in d:
                    d[i - j].append(mat[i][j])
                else:
                    d[i - j] = [mat[i][j]]
        # Now we need to sort the diagonals 
        for k in d.values():
            k.sort(key = lambda x:-x)
        for i in range(row):
            for j in range(col):
                mat[i][j] = d[i - j].pop()
        return mat
            
sol = Solution()
print sol.sort_diagonal([[3,3,1,1],[2,2,1,2],[1,1,1,2]])
            
        