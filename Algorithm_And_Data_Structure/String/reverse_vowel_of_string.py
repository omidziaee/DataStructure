'''
Created on Jan 20, 2019

@author: omid
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # We need to consider four cases:
        # 1) both the left pointer and right pointer are vowels 2) left is vowel and right is not
        # 3) right is vowel and left is not 4) non of them is vowel
        # SUPER IMPORTANT!! after checking each condition put continue otherwise it goes and checks for 
        # the other if statement!!!
        if len(s) <= 1:
            return s
        s_list = list(s)
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        right_pointer = len(s) - 1
        left_pointer = 0
        while left_pointer < right_pointer:
            if s_list[left_pointer] in vowel_set and s_list[right_pointer] in vowel_set:
                temp = s_list[left_pointer]
                s_list[left_pointer] = s_list[right_pointer]
                s_list[right_pointer] = temp
                right_pointer -= 1
                left_pointer += 1
                continue
            if s_list[left_pointer] in vowel_set and s_list[right_pointer] not in vowel_set:
                right_pointer -= 1
                continue
            if s_list[right_pointer] in vowel_set and s_list[left_pointer] not in vowel_set:
                left_pointer += 1
                continue
            if s_list[left_pointer] not in vowel_set and s_list[right_pointer] not in vowel_set:
                left_pointer += 1
                right_pointer -= 1
                continue
        return ''.join(s_list)
    
sol = Solution()
print sol.reverseVowels("hello")
