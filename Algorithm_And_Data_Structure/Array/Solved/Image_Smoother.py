'''
Created on Sep 27, 2018

@author: USOMZIA
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes
 the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as 
 many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # The idea is nice and easy to understand. We need to traverse the array and 
        # check exactly where we are. If it is possible and all the 8 suronding indices
        # have value or we are in boundries. So we need a counter for counting the existance
        # of surronding of cells.
        number_of_rows = len(M)
        number_of_columns = len(M[0])
        # Create and initilize the result list
        
        result = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                # Now we check all the surronding elements and count them
                counter_of_surroundings = 0
                for surrounding_rows in (row_index - 1, row_index, row_index + 1):
                    for surrounding_columns in (column_index - 1, column_index, column_index + 1):
                        # Now we need to check if surroundings exist
                        if 0 <= surrounding_rows < number_of_rows and 0 <= surrounding_columns < number_of_columns:
                            result[row_index][column_index] += M[surrounding_rows][surrounding_columns]
                            counter_of_surroundings += 1
                result[row_index][column_index] /= counter_of_surroundings
        return result
    def image_smoother(self, image):
        rows = len(image)
        cols = len(image[0])
        smooth_image = [[0 for _ in range(cols)] for _ in range(rows)]
        # Traverse the matrix
        for i in range(rows):
            for j in range(cols):
                sum_num = 0
                counter = 0
                if i > 0:
                    counter += 1
                    sum_num += image[i - 1][j] 
                    if j > 0:
                        counter += 1
                        sum_num += image[i - 1][j - 1]
                    if j < cols - 1:
                        counter += 1
                        sum_num += image[i - 1][j + 1]
                if i < rows - 1:
                    counter += 1
                    sum_num += image[i + 1][j]
                    if j < cols - 1:
                        counter += 1
                        sum_num += image[i + 1][j + 1]
                    if j > 0:
                        counter += 1
                        sum_num += image[i + 1][j - 1]
                if j > 0:
                    counter += 1
                    sum_num += image[i][j - 1]
                if j < cols - 1:
                    counter += 1
                    sum_num += image[i][j + 1]
                sum_num += image[i][j]
                # plus one is because of itself
                smooth_image[i][j] = sum_num / (counter + 1)
        return smooth_image
A = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]    
sol = Solution()
print sol.image_smoother(A)
                            
                            
                            
                
                            
                        
        
