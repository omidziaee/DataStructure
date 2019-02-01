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
                result.append(first_char + combination_other)
                
        return result
        
        
    
    
sol = Solution()
print sol.letterCasePermutation("a1b2")
                    