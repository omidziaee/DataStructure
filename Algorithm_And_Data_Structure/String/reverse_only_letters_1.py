'''
Created on Jan 17, 2019

@author: omid
Given a string_leet_code S, return the "reversed" string_leet_code where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Come on boy string_leet_code is immutable you should convert it to a list!
        # We need to consider four cases:
        # 1) both left and right are alphabet 2) left is alpha right is not
        # 3) left is not right is 4) not of them are alphabet
        S_list = list(S)
        right_pointer = len(S_list) - 1
        left_pointer = 0
        while left_pointer < right_pointer:
            if S_list[left_pointer].isalpha() and S_list[right_pointer].isalpha():
                temp = S_list[left_pointer]
                S_list[left_pointer] = S_list[right_pointer]
                S_list[right_pointer] = temp
                right_pointer -= 1
                left_pointer += 1
                continue
            if S_list[left_pointer].isalpha() and (not S_list[right_pointer].isalpha()):
                right_pointer -= 1
                continue
            if S_list[right_pointer].isalpha() and (not S_list[left_pointer].isalpha()):
                left_pointer +=1
                continue
            if (not S_list[left_pointer].isalpha()) and (not S_list[right_pointer].isalpha()):
                left_pointer += 1
                right_pointer -= 1
                continue
        return ''.join(S_list)
                
                
sol = Solution()
print sol.reverseOnlyLetters("7_28]")
