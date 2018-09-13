'''
Created on Aug 23, 2018

@author: USOMZIA
'''

def binearySearch(arr, k):
    
    #Base case
    if len(arr) == 0:
        return False
    mid = len(arr) / 2
    leftSide = arr[:mid]
    rightSide = arr[mid:]
    
    if k > arr[mid]:
        return binearySearch(rightSide, k)
    elif k < arr[mid]:
        return binearySearch(leftSide, k)
    else:
        return True
    
print binearySearch([1, 2, 3, 4, 51, 55, 57, 60], 3)