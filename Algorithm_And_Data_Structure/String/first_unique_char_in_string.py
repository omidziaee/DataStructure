'''
Created on Jan 20, 2019

@author: omid
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # We need to go over the string twice
        # 1) to create the char counter dictionary 2) to go over the string and check if the value in dic
        # is one! if the value is one return the index which for sure is the index of the first unique char
        if len(s) == 0:
            return -1
        char_count_dic = {}
        for char in s:
            if char in char_count_dic:
                char_count_dic[char] += 1
            else:
                char_count_dic[char] = 1
        for index, char in enumerate(s):
            if char_count_dic[char] == 1:
                return index
        return -1
