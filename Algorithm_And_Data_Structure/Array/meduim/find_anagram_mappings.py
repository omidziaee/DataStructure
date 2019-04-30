'''
Created on Feb 10, 2019

@author: omid
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
'''
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        dic_location_B = {}
        for i, num in enumerate(B):
            if num in dic_location_B:
                dic_location_B[num].append(i)
            else:
                dic_location_B[num] = [i]
        for A_num in A:
            result.append(dic_location_B[A_num][0])
        return result
