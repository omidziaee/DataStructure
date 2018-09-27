'''
Created on Sep 5, 2018

@author: USOMZIA
'''
class Solution(object):
    def separation(self, arr):
        evens = []
        odds = []
        for elem in arr:
            if elem % 2 != 0:
                odds.append(elem)
            else:
                evens.append(elem)
        return evens + odds
sol = Solution()
print sol.separation([4,3,5,2])    

 
        
