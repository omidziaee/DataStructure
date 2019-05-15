'''
Created on Jan 20, 2019

@author: omid
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Edge cases
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        # This is dictionary to map close and open paranthesis
        open_close_dic = {'(': ')', '{': '}','[': ']'}
        # This is a stack to keep the open paranthsis
        stack_keep_open = []
        # Traverse over the string
        for char in s:
            # Check if the char is an open paran
            if char in open_close_dic:
                # If yes add it to the open paran stack
                stack_keep_open.append(char)
            # If not check that if the last open paran matches this close or check if the length of open stack
            # is zero in this case we have a close paran but there is no any open paran to match it!
            elif len(stack_keep_open) == 0 or char != open_close_dic[stack_keep_open.pop()]:
                return False
        # Finally check if the open stack is empty if it is not it means that open and close parans are not
        # match
        return len(stack_keep_open) == 0
    
sol = Solution()
print sol.isValid("){")
