'''
Created on Aug 12, 2019

@author: USOMZIA
'''
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        # This is easy just create two new one D arrays to keep the number of B in each one
        if not picture:
            return 0
        rows = len(picture)
        cols = len(picture[0])
        row_one_count = [0 for _ in range(rows)]
        col_one_count = [0 for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    row_one_count[i] += 1
                    col_one_count[j] += 1
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B' and row_one_count[i] == 1 and col_one_count[j] == 1:
                    counter += 1
        return counter
    def findLonelyPixel_rec(self, picture):
        if not picture:
            return 0
        rows = len(picture)
        cols = len(picture)
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    if self.helper(picture, i, j):
                        counter += 1
        return counter
    def helper(self, picture, x, y):
        #base case
        if x < 0 or x > len(picture) - 1 or y < 0 or y > len(picture[0]):
            return False
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x, y
            while (nx + direction[0] >= 0 and nx + direction[0] < len(picture) and ny + direction[1] >= 0 and ny + direction[1] < len(picture[0])):
                nx += direction[0]
                ny += direction[1]
                if picture[nx][ny] == 'B':
                    return False
        return True
            
                    
    
picture = [['W', 'W', 'B'],
 ['W', 'W', 'B'],
 ['B', 'W', 'W']]

sol = Solution()
print sol.findLonelyPixel_rec(picture)
                        
                        
                        
                        
