'''
Created on Nov 6, 2019

@author: USOMZIA
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function 
to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers 
have at least h citations each, and the other N-h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''
class Solution(object):
    def hIndex_counting(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        max_cite = max(citations)
        # Including maximum
        count = [0 for _ in range(max_cite + 1)]
        for elem in citations:
            count[elem] += 1
        k = 0
        for i in range(len(count) - 1, -1, -1):
            k += count[i]
            if k >= i:
                return i
        return 0
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        citations.sort()
        k = 0
        for i in range(len(citations) - 1, -1, -1):
            if k < citations[i]:
                k += 1
            if k >= citations[i]:
                return k
        return k