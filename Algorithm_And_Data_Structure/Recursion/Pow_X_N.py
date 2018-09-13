'''
Created on Aug 16, 2018

@author: USOMZIA
'''
def powXN(x, n):
    if n == 0:
        return 1
    half = powXN(x, n / 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
    
def myPowXN(x, n):
    if n < 0:
        x = 1 / x
        n = -n
        
        return powXN(x, n)
    
print powXN(5, 7)