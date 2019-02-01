'''
Created on Jan 31, 2019

@author: USOMZIA
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''
class Solution(object):
    def letterCasePermutation(self, S):
        if len(S) <= 1:
            return S
        first_char = S[0]
        result = []
        combinations_other = self.letterCasePermutation(S[1:])
        for combination_other in combinations_other:
            if first_char.isalpha():
                result.append(first_char.upper() + combination_other) 
                result.append(first_char.lower() + combination_other)
            else:
                # This line is crucial otherwise it returns an empty list
                # Without this line it eliminates the backtrack meaning 
                # reslut will remain empty (look at the body of the function) and 
                # when it returns to the combination_other it returns an empty list!!!
                result.append(first_char + combination_other)
                
        return result
        
        
    
    
sol = Solution()
print sol.letterCasePermutation("a1b2")