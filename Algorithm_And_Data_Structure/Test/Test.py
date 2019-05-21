class Solution():
    def rotate_in_place(self, matrix):
        if len(matrix) == 0:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # Now reverse the elements of each row
        # Here it is a matrix but in general no
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            self.reverse_row(matrix[i])
        return matrix
    def reverse_row(self, row):
        right = len(row) - 1
        left = 0
        while left <= right:
            temp = row[left]
            row[left] = row[right]
            row[right] = temp
            left += 1
            right -= 1
    
sol = Solution()
print sol.rotate_in_place([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            