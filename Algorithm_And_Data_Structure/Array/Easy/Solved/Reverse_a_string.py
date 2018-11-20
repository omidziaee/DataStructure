'''
Created on Nov 17, 2018

@author: omid
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        right_pointer = len(s1) - 1
        left_pointer = 0
        while left_pointer < right_pointer:
            temp = s1[right_pointer]
            s1[right_pointer] = s1[left_pointer]
            s1[left_pointer] = temp
            left_pointer += 1
            right_pointer -=1
        return ''.join(s1)
    
    def reverse_string_recursive(self, s):
        if len(s) == 1:
            return s
        return s[-1] + self.reverse_string_recursive(s[:-1])
    
    
       
sol = Solution()
print sol.reverseString("hello")
print sol.reverse_string_recursive("omid, ziaee")