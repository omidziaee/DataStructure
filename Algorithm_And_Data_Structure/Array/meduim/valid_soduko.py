'''
Created on Nov 8, 2019

@author: USOMZIA
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = len(board[0])
        rows = len(board)
        for i in range(rows):
            row_send = []
            for j in range(cols):
                row_send.append(board[i][j])
            if not self.is_valid(row_send):
                return False
        for j in range(cols):
            col_send = []
            for i in range(rows):
                col_send.append(board[i][j])
            if not self.is_valid(col_send):
                return False
        square = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                #square = [board[k][l] for k in range(i, i+3) for l in range(j, j+3)]
                square = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        square.append(board[k][l]) 
                if not self.is_valid(square):
                    return False
        return True
    
    def is_valid(self, arr):
        arr_set = set()
        for elem in arr:
            if elem != ".":
                elem = int(elem)
                if 0 < elem <= 9:
                    if elem not in arr_set:
                        arr_set.add(elem)
                    else:
                        return False
                else:
                    return False
        return True
            
'''            
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."], 
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"], 
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"], 
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"], 
         [".",".",".",".","8",".",".","7","9"]]
'''
board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]
sol = Solution()
print sol.isValidSudoku(board)