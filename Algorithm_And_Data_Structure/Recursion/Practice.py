'''
Created on Sep 20, 2018

@author: USOMZIA
'''
# string break is like abc acb bac ...

def stringBreak(s):
    
    #base case
    if len(s) == 1:
        return s
    head = s[0] 
    rest = stringBreak(s[1:])


s = "abc"
print stringBreak(s)

