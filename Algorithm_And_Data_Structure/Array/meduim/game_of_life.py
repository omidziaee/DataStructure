'''
Created on Sep 27, 2019

@author: USOMZIA
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell 
interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules 
(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        rows = len(board)
        cols = len(board[0])
        # Hey be carfule do not put copy_board = board this is not the case for arrays in any language
        #import copy
        #copy_board = copy.deepcopy(board)
        copy_board = [[board[i][j] for j in range(cols)] for i in range(rows)] # best way to copy the list in any dimension
        # The following wont work because it is shallow copy it means that it just copy the outer list not the inner list which means 
        # if you change the inner list however in some place it works
        #copy_board = board[:][:]
        for i in range(rows):
            for j in range(cols):
                one_counter = 0
                for cnt_row in (i - 1, i, i + 1):
                    for cnt_col in (j - 1, j, j + 1):
                        # This one is necassary as we do not want to exceed the limits of arrays
                        if 0 <= cnt_row < rows and 0 <= cnt_col < cols and copy_board[cnt_row][cnt_col] == 1:
                            one_counter += 1
                # We add the cell in the middle as well however we are just looking for prepherals
                one_counter -= copy_board[i][j]
                if copy_board[i][j] == 1 and one_counter < 2 or one_counter > 3:
                    board[i][j] = 0
                if copy_board[i][j] == 0 and one_counter == 3:
                    board[i][j] = 1
                    
    def gameOfLife_noExtraSpace(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                one_counter = 0
                for cnt_row in (i - 1, i, i + 1):
                    for cnt_col in (j - 1, j, j + 1):
                        # This one is necassary as we do not want to exceed the limits of arrays
                        if 0 <= cnt_row < rows and 0 <= cnt_col < cols:
                            one_counter += board[cnt_row][cnt_col] & 1
                # We add the cell in the middle as well however we are just looking for prepherals
                #one_counter -= board[i][j] & 1
                if one_counter == 3 or one_counter - board[i][j] == 3:
                    board[i][j] |= 2
        for i in range(rows):
            for j in range(cols):
                board[i][j] >>= 1
                    