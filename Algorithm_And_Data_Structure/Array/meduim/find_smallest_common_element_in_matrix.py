'''
Created on Sep 23, 2019

@author: omid
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
'''
class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        import bisect
        for elem in mat[0]:
            counter = 0
            for i in range(1, len(mat)):
                index = bisect.bisect_right(mat[i], elem)
                if index > 0 and mat[i][index - 1] == elem:
                    counter += 1
                else:
                    break
            if counter == len(mat) - 1:
                return elem
        return -1
    
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
sol = Solution()
print sol.smallestCommonElement(mat)