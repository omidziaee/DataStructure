'''
Created on Nov 22, 2019

@author: USOMZIA
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length 
to make the original string s balanced.
Return 0 if the string is already balanced.

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
'''
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        counter = 0
        len_forth = len(s) / 4
        dic_map = {"Q":0, "W":0, "R":0, "E":0}
        for ch in s:
            dic_map[ch] += 1
        

sol = Solution()
print sol.balancedString("QQQE")