'''
Created on Jul 31, 2019

@author: USOMZIA
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 
represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board 
to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom 
at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

 

Example:

Input:
board = 
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

Explanation: 
https://leetcode.com/problems/candy-crush/
'''
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(board)
        cols = len(board[0])
        #This boolean is to show we make a crush so this might result in new crush and we need to search the board again
        todo = False
        
        # It is possible to use another board and after the first traverse to check 
        # check for each row if 3 columns in a row is the same. The trick is start from zero but goes up to cols - 2!!
        for i in range(rows):
            for j in range(cols - 2):
                # we need to check the abs as we might convert them to negative in the previous step
                if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    todo = True
        # Now traverse the board to check for the rows
        for i in range(rows - 2):
            for j in range(cols):
                if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    todo = True
                    
        # Now traverse the board for the last time to move the crushed 
        # two pointers r for read and wr for write so we traverse each column backward to check the negative cells
        # if it is positive moving all the cells down is hard always writting backward is easier
        for c in range(cols):
            wr = rows - 1
            for r in range(rows - 1, -1, -1):
                # Check the content of the cell if it is positive just write the content of the board to that cell
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    # Move the write index
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
                
        # Now if todo is true again run the check else return the board
        return self.candyCrush(board) if todo else board

board = [[20, 21, 22], [1, 2, 3], [1, 4, 5], [1, 6, 7], [8, 9, 10]]
sol = Solution()
print sol.candyCrush(board)