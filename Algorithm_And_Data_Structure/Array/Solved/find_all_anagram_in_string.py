'''
Created on May 4, 2019

@author: omid
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic_p = [0] * 26
        dic_s = [0] * 26
        res = []
        for i in range(len(p)):
            dic_p[ord(p[i]) - ord('a')] += 1
            dic_s[ord(s[i]) - ord('a')] += 1
        if dic_p == dic_s:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            # s[i - 1] because we are adding the s[i] so we need
            # to reduce the previous one as the window is moving
            dic_s[ord(s[i - 1]) - ord('a')] -= 1
            dic_s[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if dic_s == dic_p:
                res.append(i)
        return res