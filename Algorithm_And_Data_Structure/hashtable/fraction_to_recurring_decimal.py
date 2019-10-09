'''
Created on Oct 4, 2019

@author: omid
Given two integers representing the numerator and denominator of a fraction, return 
the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''
class Solution():
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # This problem the important thing is edge cases
        if denominator == 0:
            return None
        res = ""
        # we do this to overcome the overlaping case for positive integers
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        frac = numerator / denominator
        if numerator % denominator == 0:
            return res + str(frac)
        res += str(frac) + "." # . is for start of decimal point
        # the first decimal point
        numerator %= denominator
        # keep the length of res
        l = len(res)
        # Now create a hash table to keep the place of the decimal and the value of it
        table = {}
        # The idea is keep the numerator like 3/4 we keep 3 then as we move forward
        # we know if we face 3 as numerator again the result would be the same
        # Now simulate the decimal division; 
        while numerator != 0:
            # if it is already in table it means it is repeated
            if numerator not in table:
                table[numerator] = l
            else:
                # take the index of the last same numerator
                l = table[numerator]
                # If it already exists it means it is repeated
                res = res[:l] + "(" + res[l:] + ")"
                return res
            # Now multiply numerator by 10 like 3 divide by 4 then multiply 3 by 10
            numerator *= 10
            res += str(numerator / denominator)
            numerator %= denominator
            l += 1
        return res
            
                
    
sol = Solution()
print sol.fractionToDecimal(-50, 8)