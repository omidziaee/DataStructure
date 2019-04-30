'''
Created on Aug 14, 2018

@author: USOMZIA
'''

class Solution(object):
    def permutation(self, s):
        # we need to go over the string_leet_code and for each char find the permutation of the rest of the string_leet_code
        # for example for abc set aside b and find all the permutaiton for ac and append it to b and 
        # so on so force
        # You can not have a list defined and then append to it
        out = []
        # Base case
        if len(s) == 1:
            out = [s]
        else:
            # Set aside the char and permute on the rest of the string_leet_code
            for i, let in enumerate(s):
            # Permute on the rest of the string_leet_code basically we skip the char in ith position
                for perm in  self.permutation(s[:i] + s[i+1:]):
                    out += [let + perm]
        return out
    def get_permutations(self,string):

    # Generate all permutations of the input string_leet_code
    #base case
        if len(string) <= 1:
            return set([string])
        perm_list = []
        for index in range(len(string)):
            head_of_perm = string[index]
            tail_of_perm = self.get_permutations(string[:index] + string[index + 1:])
        for perm in tail_of_perm:
            perm_list.append(head_of_perm + perm)
    
        

        return set(perm_list)
    
sol = Solution()
print sol.get_permutations('abc')
    