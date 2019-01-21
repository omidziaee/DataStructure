'''
Created on Jan 20, 2019

@author: omid
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note: Palindrome means that the string is symetrical
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # In place string manipulation can be done just if you convert it to list
        # check it twice once for the left char that makes difference another time for the
        # right one that makes difference
        s_list = list(s)
        if len(s) < 2:
            return True
        left_pointer = 0
        right_pointer = len(s) - 1
        one_char_diff_1 = 0
        while left_pointer < right_pointer and one_char_diff_1 < 2:
            # As far as one difference found remove it (here the right one) and again check if
            # the new one without the removed char is palindrome
            if s_list[left_pointer] != s_list[right_pointer]:
                one_char_diff_1 += 1
                # remove the right char
                s_list = s_list[:right_pointer] + s_list[right_pointer + 1:]
                # restart the pointers 
                left_pointer = 0
                right_pointer = len(s_list) - 1
            else:
                left_pointer += 1
                right_pointer -= 1
        # Now do the same for the left char
        s_list = list(s)
        left_pointer = 0
        right_pointer = len(s) - 1
        one_char_diff_2 = 0
        while left_pointer < right_pointer and one_char_diff_2 < 2:
            if s_list[left_pointer] != s_list[right_pointer]:
                one_char_diff_2 += 1
                s_list = s_list[:left_pointer] + s_list[left_pointer + 1:]
                left_pointer = 0
                right_pointer = len(s_list) - 1
            else:
                left_pointer += 1
                right_pointer -= 1        
                        
        return one_char_diff_1 < 2 or one_char_diff_2 < 2
        
    
sol = Solution()
print sol.validPalindrome("abcdfa")