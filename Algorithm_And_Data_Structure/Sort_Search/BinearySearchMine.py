'''
Created on Aug 23, 2018

@author: USOMZIA
'''
from win32con import NULL
def binearySearchMine(arr, k):
    if len(arr) == 0:
        return False
    found = False
    leftSide = [0]
    rightSide = [0]
    
    while not found and ((len(leftSide) != 0) and (len(rightSide) != 0)):
        mid = len(arr) / 2
        leftSide = arr[:mid]
        rightSide = arr[mid:]
        
        if k == leftSide[-1] or k == rightSide[0]:
            found = True 
        else:
            if k < leftSide[-1]:
                arr = leftSide
            elif k > rightSide[0]:
                arr = rightSide
            else:
                return False
                
    return found

print binearySearchMine([1, 2, 3, 4, 51, 55, 57, 60], 3)
        