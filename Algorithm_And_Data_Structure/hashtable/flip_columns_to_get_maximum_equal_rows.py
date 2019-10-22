'''
Created on Oct 21, 2019

@author: USOMZIA
Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every 
cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.
Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
'''
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # key point is 
        # 1) a ^ 0 = a and a ^ 1 = not(a)
        # 2) Here we are looking for patterns; 110 and 001 both are aab 
        if not matrix:
            return 0
        dic = {}
        for row in matrix:
            pattern = []
            for elem in row:
                modified_elem = elem ^ row[0]
                pattern.append(modified_elem)
            key = tuple(pattern)
            # Now count the similar patterns
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        return max(dic.values())
    def maxEqualRowsAfterFlips_shorter(self, matrix):
        import collections
        if not matrix:
            return 0
        dic = collections.defaultdict(int)
        for row in matrix:
            pattern = []
            for elem in row:
                modified = elem ^ row[0]
                pattern.append(modified)
            dic[tuple(pattern)] += 1
        return max(dic.values())
    
    def maxEqualRowsAfterFlips_shorter_v(self, matrix):
        import collections
        if not matrix:
            return 0
        pat = []
        for row in matrix:
            pattern = []
            for elem in row:
                modified = elem ^ row[0]
                pattern.append(modified)
            pat.append(tuple(pattern))
        return max(collections.Counter(pat).values())
                
                
    
    
                