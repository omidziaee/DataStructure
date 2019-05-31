'''
Created on May 25, 2019

@author: omid
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()
        s_list = list(s)
        start = 0
        end = len(s) - 1
        # first reverse the whole string
        self.reverse_str(start, end, s_list)
        # now reverse each word
        slow_pointer = 0
        for i in range(len(s_list) + 1):
            # we need to check for both spae and the end of the string
            if i == len(s_list) or s_list[i] == ' ':
                self.reverse_str(slow_pointer, i - 1, s_list)
                slow_pointer = i + 1
        res = ''.join(s_list)
        return ' '.join(res.split())
    def reverse_str(self, start, end, s):
        while start <= end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1