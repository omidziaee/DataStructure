'''
Created on Jun 20, 2019

@author: USOMZIA
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # It is a dp problem
        # G[n] is the number of possible BST from 1 to n 
        G = [0 for _ in range(n + 1)]
        G[0] = 1 # if the length is zero there is just one tree None
        G[1] = 1 # if the length is one there is just one root node no left or right
        for i in range(2, n + 1):
            # we are looking for the number of possible BSTs up to length i included so loop 
            # should go up to i + 1
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]