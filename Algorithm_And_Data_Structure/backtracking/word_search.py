'''
Created on Jul 4, 2019

@author: omid
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        find = False
        for i in range(rows):
            for j in range(cols):
                find = self.dfs(board, word, i, j)
                if find:
                    return True
        return False
    def dfs(self, board, word, i, j):
        if not board:
            return False
        if len(word) == 0:
            return True
        else:
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or word[0] != board[i][j]:
                return False
            # this is to prevent to visit on cell more than once as we traverse all four directions
            temp = board[i][j]
            board[i][j] = "#"
            # now traverse on any direction and one of them should be correct
            res = self.dfs(board, word[1:], i - 1, j) or  \
                  self.dfs(board, word[1:], i + 1, j) or  \
                  self.dfs(board, word[1:], i, j - 1) or  \
                  self.dfs(board, word[1:], i, j + 1)
            # now return the board[i][j] to its original value
            board[i][j] = temp
        return res
    

sol = Solution()
board = [['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']]
print sol.exist(board, "SEE")
                