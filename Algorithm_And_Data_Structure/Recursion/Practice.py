<<<<<<< HEAD
'''
Created on Sep 20, 2018

@author: USOMZIA
'''
# string_leet_code break is like abc acb bac ...

def stringBreak(s):
    
    #base case
    if len(s) == 1:
        return s
    head = s[0] 
    rest = stringBreak(s[1:])


s = "abc"
print stringBreak(s)

=======
'''
Created on Sep 20, 2018

@author: USOMZIA
'''
# string_leet_code break is like abc acb bac ...

def stringBreak(s):
    
    #base case
    if len(s) == 1:
        return s
    head = s[0] 
    rest = stringBreak(s[1:])


s = "abc"
print stringBreak(s)

>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
