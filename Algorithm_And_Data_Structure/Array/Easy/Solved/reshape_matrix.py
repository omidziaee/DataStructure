'''
Created on May 3, 2019

@author: omid
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
'''
class Solution():
    def matrixReshape_naive(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])
        if rows * cols != r * c:
            return nums
        one_d_arr = []
        new_matrix = [[None for _ in range(c)] for _ in range(r)]
        for i in range(rows):
            one_d_arr += nums[i]
        if r == 1:
            return one_d_arr
        row = 0
        col = 0
        for i in range(len(one_d_arr)):
            if i % c == 0 and i != 0:
                row += 1
                col = 0
                new_matrix[row][col] = one_d_arr[i]
                col += 1
            else:
                new_matrix[row][col] = one_d_arr[i]
                col += 1
        return new_matrix
    
    # It is easy! rows are the one_D_arr iterator divided by c and columns are one_D_arr iterator
    # residual to c
    def matrixReshape_better(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])
        if rows * cols != r * c:
            return nums
        one_d_arr = []
        for i in range(rows):
            one_d_arr += nums[i]
        if r == 1:
            return one_d_arr
        new_matrix = [[0 for _ in range(c)] for _ in range(r)]
        row = 0
        col = 0
        for i in range(len(one_d_arr)):
            new_matrix[i / c][i % c] = one_d_arr[i]      
        return new_matrix
    
    # With queue; this is very similar to change it to one dimensional arry but the differene is you do
    # not need to loop over the one dimensional array like the naive solution
    def matrixReshape_queue(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        import collections
        one_d_q = collections.deque()
        if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
            return nums
        new_matrix = [[None for _ in range(c)] for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                one_d_q.append(nums[i][j])
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = one_d_q.popleft()
        return new_matrix
    # Without extra space for making it one_D
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Here we traverse over the real matrix then as soon as the col
        # counter reaches c we reset it and add one to row counter
        if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
            return nums
        row = 0
        col = 0 
        new_matrix = [[None for _ in range(c)] for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                new_matrix[row][col] = nums[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1
        return new_matrix
    
sol = Solution()
print sol.matrixReshape([[1, 2], [3, 4]], 1, 4)