'''
Created on Apr 23, 2019

@author: USOMZIA
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        sum_num = 0
        carry_over = 0
        res = []
        while i >= 0 and j >= 0:
            sum_num = int(num1[i]) + int(num2[j]) + carry_over
            if sum_num > 9:
                carry_over = sum_num / 10
                sum_num %= 10
            else:
                carry_over = 0
            res.insert(0, str(sum_num))
            i -= 1
            j -= 1
        while i >= 0:
            sum_num = int(num1[i]) + carry_over
            if sum_num > 9:
                carry_over = sum_num / 10
                sum_num %= 10
            else:
                carry_over = 0
            res.insert(0, str(sum_num))
            i -= 1
        while j >= 0:
            sum_num = int(num2[j]) + carry_over
            if sum_num > 9:
                carry_over = sum_num / 10
                sum_num %= 10
            else:
                carry_over = 0
            res.insert(0, str(sum_num))
            j -= 1
        if carry_over > 0:
            res.insert(0, str(carry_over))
        return ''.join(res)
            
            
sol = Solution()
print sol.addStrings("9", "99")