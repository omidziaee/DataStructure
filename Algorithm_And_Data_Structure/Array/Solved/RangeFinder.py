<<<<<<< HEAD
'''
Created on Aug 23, 2018

@author: USOMZIA
'''

def rangeFinder(arr):
    start = 0
    end = 0
    gap = {}
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 1:
            end = i + 1
        gap[i] = arr[end] - arr[start]
        start = i
        
    return gap

=======
'''
Created on Aug 23, 2018

@author: USOMZIA
'''

def rangeFinder(arr):
    start = 0
    end = 0
    gap = {}
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 1:
            end = i + 1
        gap[i] = arr[end] - arr[start]
        start = i
        
    return gap

>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print rangeFinder([1, 2, 3, 7, 8, 9, 14])