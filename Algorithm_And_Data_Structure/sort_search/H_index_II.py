'''
Created on Nov 6, 2019

@author: USOMZIA
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.
According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at 
least h citations each, and the other N - h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
'''
class Solution(object):
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
        l = 0
        r = len(citations) - 1
        while l <= r:
            mid = l + (r - l) / 2
            val = citations[mid]
            if val < len(citations) - mid:
                l = mid + 1
            elif val > len(citations) - mid:
                r = mid - 1
            elif val == len(citations) - mid:
                return len(citations) - mid
        return len(citations) - l

citations = [0,1,3,5,6]
sol = Solution()
print sol.hIndex(citations)