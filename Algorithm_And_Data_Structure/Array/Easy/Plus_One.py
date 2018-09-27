'''
Created on Sep 25, 2018

@author: USOMZIA
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carryOver = 0
        digitLen = len(digits) - 1
        final = []
        while digitLen >= 0:
            if digitLen == len(digits) - 1:
                result = digits[digitLen] + 1
            else:
                result = digits[digitLen] + carryOver    
            carryOver = 0
            if result >= 10:
                carryOver = 1
                result %= 10
            final.insert(0, result)
            digitLen -= 1
        if carryOver == 1:
            final.insert(0, carryOver)
        return final
            
            
sol = Solution()
print sol.plusOne([9,9,9])