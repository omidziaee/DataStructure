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
        j = len(digits) - 1
        final = []
        while j >= 0:
            if j == len(digits) - 1:
                result = digits[j] + 1
            else:
                result = digits[j] + carryOver
            if result >= 10:
                carryOver = 1
                result %= 10
            final.insert(0, result)
            j -= 1
        if carryOver == 1 and result == 0:
            final.insert(0, carryOver)
        return final
            
            
sol = Solution()
print sol.plusOne([1,2,9])