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
    # The following works fine if the length of the string is known but if it is a string stream the story is different
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
    
    # This works when the string is not pre known meaning if it is string stream and it comes by
    # In this case each new char goes through the dic count and then remove from the list if it is 
    # repeating
    def firstUniqueChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return -1
        dic_char_count = {}
        uniqu_char = []
        for char in s:
            if char in dic_char_count:
                dic_char_count[char] += 1
            else:
                dic_char_count[char] = 1
                uniqu_char.append(char)
        for char in dic_char_count:
            if dic_char_count[char] > 1:
                uniqu_char.remove(char)
        return s.index(uniqu_char[0]) if len(uniqu_char) > 0 else -1
