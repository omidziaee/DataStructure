'''
Created on Aug 14, 2018

@author: USOMZIA
'''

class Solution(object):
    def permutation(self, s):
        # we need to go over the string and for each char find the permutation of the rest of the string
        # for example for abc set aside b and find all the permutaiton for ac and append it to b and 
        # so on so force
        # You can not have a list defined and then append to it
        out = []
        # Base case
        if len(s) == 1:
            out = [s]
        else:
            # Set aside the char and permute on the rest of the string
            for i, let in enumerate(s):
            # Permute on the rest of the string basically we skip the char in ith position
                for perm in  self.permutation(s[:i] + s[i+1:]):
                    out += [let + perm]
        return out
    
sol = Solution()
    