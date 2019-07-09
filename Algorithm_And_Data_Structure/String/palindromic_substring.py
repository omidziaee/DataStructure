'''
Created on Jul 8, 2019

@author: USOMZIA
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # lets say the string is aaa then the center of the palindrome can be a#a#a either characte
        # a or # meaning the character or between characters. The 2N-1 comes from this description.
        # So from each center we need to expand around it to find a new palindrom
        N = len(s)
        ans = 0
        res = []
        for center in range(2*N - 1):
            # Now define the two edges of the palindrome
            # If center is even then left and right are the same
            # If center is odd then right is one more than left
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                # When s[left] == s[right] then it is palindrome 
                ans += 1
                # Before moving left and right it is needed to append it to the result
                res.append(s[left: right + 1])
                left -= 1
                right += 1
        return res
sol = Solution()
print sol.countSubstrings("cbbd")