<<<<<<< HEAD
'''
Created on Nov 17, 2018

@author: omid
Write a function that takes a string_leet_code as input and returns the string_leet_code reversed.

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
=======
'''
Created on Nov 17, 2018

@author: omid
Write a function that takes a string_leet_code as input and returns the string_leet_code reversed.

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
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print sol.reverse_string_recursive("omid, ziaee")