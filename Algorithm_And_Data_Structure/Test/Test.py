<<<<<<< HEAD
class Solution(object):
    def find_permutations(self, main_string):
        if len(main_string) == 1:
            return main_string
        head = main_string[0]
        remain_string = main_string[1:]
        perms = []
        for i in range(len(remain_string)):
            perms.append(self.find_permutations(remain_string))
            
        for i in range(len(perms)):
            perms[i] = ''.join((head + perms[i]))
        return perms
    
sol = Solution()
print sol.find_permutations('abc')
            
=======
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
                    
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git
