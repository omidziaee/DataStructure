'''
Created on Sep 26, 2019

@author: USOMZIA
Given a picture consisting of black and white pixels, and a positive integer N, find the 
number of black pixels located at some specific row R and column C that align with all 
the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black 
and white pixels respectively.

Example:
Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index
Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.
'''
class Solution():
    def findBlackPixel_not_complete(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture:
            return 0
        counter = 0
        for i in range(len(picture)):
            for j in range(len(picture[0]) - 1):
                if self.calc_B(picture, i, j):
                    counter += 1
        return counter
    
    def calc_B(self, N, row, col):
        col_count = row_count = 0
        N_col = []
        for i in range(len(N[row])):
            if N[row][i] == 'B':
                row_count += 1
        for j in range(len(N)):
            N_col.append(N[j][col])
        for j in range(len(N_col)):
            if N[j][col] == 'B':
                col_count += 1
        return row_count == col_count
    
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        r_no = len(picture)
        c_no = len(picture[0])
        search_r = [i for i in range(r_no) if picture[i].count('B')==N]
        search_c = [i for i in range(c_no) if [j[i] for j in picture].count('B')==N]
        count = 0
        for r in search_r:
            for c in search_c:
                if picture[r][c] == 'B':
                    cur_row = picture[r]
                    sibs = filter(lambda x:x[c]=='B', picture)
                    if all([s==cur_row for s in sibs]):
                        count += 1
        return count
        
picture = [['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 
N = 3
sol = Solution()
print sol.findBlackPixel(picture, N)