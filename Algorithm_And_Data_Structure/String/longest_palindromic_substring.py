'''
Created on Jul 8, 2019

@author: USOMZIA
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        max_pal = ""
        new_pal = ""
        for center in range(2*N - 1):
            left = center / 2
            right = left + center % 2
            new_pal = self.is_palindrome(s, N, left, right)
            if len(new_pal) > len(max_pal):
                max_pal = new_pal
        return max_pal
    def is_palindrome(self, s, N, left, right):
        ans = ""
        while left >= 0 and right < N and s[left] == s[right]:
            # Before moving left and right it is needed to append it to the result
            # No need to find max here because while loop expand it as far as it can
            ans = s[left: right + 1]
            left -= 1
            right += 1
        return ans

sol = Solution()
print sol.longestPalindrome("cbbd")     