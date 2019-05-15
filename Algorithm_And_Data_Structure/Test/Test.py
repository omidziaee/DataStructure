class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # live -> dead 4
        # live -> live 3
        # dead -> dead 2
        # dead -> live 1
        rows = len(board)
        cols = len(board[0])
        counter = 0
        board_next = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if row - 1 >= 0:
                    if board[row - 1][col] % 2 == 1:
                        counter += 1
                if col - 1 >= 0:
                    if board[row][col - 1] % 2 == 1:
                        counter += 1
                if row - 1 >= 0 and col - 1>= 0:
                    if board[row - 1][col - 1] % 2 == 1:
                        counter += 1
                if row - 1 >= 0 and col + 1 <= cols - 1:
                    if board[row - 1][col + 1] % 2 == 1:
                        counter += 1
                if row + 1 <= rows - 1:
                    if board[row + 1][col] % 2 == 1:
                        counter += 1
                if col - 1 >= 0 and row + 1 <= rows - 1:
                    if board[row + 1][col - 1] % 2 == 1:
                        counter += 1
                if col + 1 <= cols - 1 and row + 1 <= rows - 1:
                    if board[row + 1][col + 1] % 2 == 1:
                        counter += 1
                if col + 1 <= cols - 1:
                    if board[row][col + 1] % 2 == 1:
                        counter += 1
                if board[row][col] % 2 == 1:
                    if counter < 2:
                        board_next[row][col] = 4
                    if counter in [2, 3]:
                        board_next[row][col] = 3
                    if counter > 3:
                        board[row][col] = 4
                if board[row][col] == 0:
                    if counter == 3:
                        board_next[row][col] = 1
                    else:
                        board_next[row][col] = 2
                counter = 0
        for row in range(rows):
            for col in range(cols):
                #board_next[row][col] &= 1
                board_next[row][col] >> 1
        return board_next
                
                    
                
sol = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print sol.gameOfLife(board)