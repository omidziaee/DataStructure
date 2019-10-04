'''
Created on Oct 4, 2019

@author: USOMZIA
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        row_A, col_A = len(A), len(A[0])
        row_B, col_B = len(B), len(B[0])
        res = [[0 for _ in range(col_B)] for _ in range(row_A)]
        table_B = {}
        for i, row in enumerate(B):
            table_B[i] = {}
            for j, elem in enumerate(row):
                if elem:
                    table_B[i][j] = elem
        for i in range(row_A):
            for j in range(col_B):
                sum_mul = 0
                for k in range(col_A):
                    sum_mul += A[i][k] * B[k][j]
                res[i][j] = sum_mul
        return res
    def multiply_find_zero(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        row_A, col_A = len(A), len(A[0])
        row_B, col_B = len(B), len(B[0])
        res = [[0 for _ in range(col_B)] for _ in range(row_A)]
        for i in range(row_A):
            for j in range(col_B):
                sum_mul = 0
                for k in range(col_A):
                    if A[i][k] and B[k][j]:
                        sum_mul += A[i][k] * B[k][j]
                res[i][j] = sum_mul
        return res
    
    def multiply_hash(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableB = {}
        for k, row in enumerate(B):
            tableB[k] = {}
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in tableB[k].iteritems():
                        C[i][j] += eleA * eleB
        return C
    
    def multiply_two_hash(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n = len(A), len(A[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        l = len(B[0])
        table_A, table_B = {}, {}
        for i, row in enumerate(A):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_A: table_A[i] = {}
                    table_A[i][j] = ele
        for i, row in enumerate(B):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_B: table_B[i] = {}
                    table_B[i][j] = ele
        C = [[0 for j in range(l)] for i in range(m)]
        for i in table_A:
            for k in table_A[i]:
                if k not in table_B: continue
                for j in table_B[k]:
                    C[i][j] += table_A[i][k] * table_B[k][j]
        return C
    
    

A = [
  [ 1, 0, 4],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 2 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
sol = Solution()
print sol.multiply_two_hash(A, B)                    