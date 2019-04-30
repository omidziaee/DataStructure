'''
Created on Aug 23, 2018

@author: USOMZIA
'''


def stringReverse(s):
     # base case
     if len(s) == 1:
         return s
     
     return s[-1] + stringReverse(s[:-1])


def stringReverseNotRec(s):
    # Note that to do this you should change the string_leet_code to the list as the string_leet_code is not mutable in python 
    s = list(s)
    if len(s) == 1:
        return s
    
    rightPointer = len(s) - 1
    leftPointer = 0
    
    while rightPointer != leftPointer:
        temp = s[leftPointer]
        s[leftPointer] = s[rightPointer]
        s[rightPointer] = temp
        rightPointer -= 1
        leftPointer += 1
    # Join the list together in order to create the new string_leet_code
    return ''.join(s)


print stringReverse("apple")
print stringReverseNotRec("apple")