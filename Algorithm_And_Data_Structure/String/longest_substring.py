'''
Created on Jul 5, 2019

@author: omid
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from Carbon.Aliases import false
class Solution(object):
    def lengthOfLongestSubstring_not(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        set_counter = set()
        for i in range(len(s)):
            if s[i] not in set_counter:
                set_counter.add(s[i])
            else:
                max_len = max(max_len, len(set_counter))
                set_counter.clear()
                set_counter.add(s[i])
        return max(max_len, len(set_counter))
    
    # This is an o(n^3)
    def lengthOfLongestSubstring_long(self, s):
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.is_unique(s, i, j):
                    max_length = max(max_length, j - i)
        return max_length
    def is_unique(self, s, start, end):
        char_set = set()
        for i in range(start, end):
            if s[i] not in char_set:
                char_set.add(s[i])
            else:
                return false
        return True
    
    def lengthOfLongestSubstring(self, s):
        fast = 0
        slow = 0
        set_char = set()
        max_length = 0
        while fast < len(s):
            if s[fast] not in set_char:
                set_char.add(s[fast])
                fast += 1
                # It is better to keep it in here then you do not need
                # to check for the case " " at the return point 
                max_length = max(max_length, fast - slow)
            else:
                while s[fast] != s[slow]:
                    set_char.remove(s[slow])
                    slow += 1
                slow += 1
                fast += 1
        return max_length
                
sol = Solution()
print sol.lengthOfLongestSubstring("pwwkew")