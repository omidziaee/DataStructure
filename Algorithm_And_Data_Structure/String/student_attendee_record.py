'''
Created on Jan 18, 2019

@author: USOMZIA
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' 
(late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        "LLPLLPLPPLLPLPLPPPLPLPLPPPLPPP"
        """
        # Three L in a row or more than one A
        if len(s) == 0:
            raise Exception("the string should not be empty!")
        counter = 0
        absent = False
        # As we start the loop from one we need to consider an edge case for the first element if it is "A"
        if s[0] == "A":
            counter += 1
            absent = True
        for index in range(1 ,len(s)):
            if s[index] == "A":
                if absent:
                    return False
                counter += 1
            if (index < len(s) - 1) and (s[index - 1] == "L") and (s[index] == "L") and (s[index + 1] == "L"):
                return False
            if counter > 1:
                return False
        return True
        
