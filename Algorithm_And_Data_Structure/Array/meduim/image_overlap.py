'''
Created on Sep 10, 2019
@author: USOMZIA
Two images A and B are given, represented as binary, square matrices of the
same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down 
any number of units), and place it on top of the other image.  After, the overlap 
of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?
Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
'''
class Solution():
    def largestOverlap_short(self, A, B):
        import collections
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
        count = collections.Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        return max(count.values() or [0])  # if the input has no 1, count will be None, that why we need or [0]
    def largestOverlap_verbose(self, A, B):
        A_ones = []
        B_ones = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A_ones.append((i, j))
                if B[i][j] == 1:
                    B_ones.append((i, j))
        dic_relevant_position = {}
        for i in range(len(A_ones)):
            for j in range(len(B_ones)):
                ax, ay = A_ones[i]
                bx, by = B_ones[j]
                if (ax - bx, ay - by) in dic_relevant_position:
                    dic_relevant_position[(ax - bx, ay - by)] += 1
                else:
                    dic_relevant_position[(ax - bx, ay - by)] = 1
        # max(dic_relevant_position.values() or [0])
        return max(max(dic_relevant_position.values(), [0]), 0)
    
A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
sol = Solution()
print sol.largestOverlap_verbose(A, B)