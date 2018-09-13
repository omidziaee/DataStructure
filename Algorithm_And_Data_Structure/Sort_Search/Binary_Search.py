'''
Created on Jul 19, 2018

@author: USOMZIA
'''
def binarySearch(arr, itemSearch):
    
    # As here the arr is fixed throughout the whole process
    # it is not possible to use the len(arr) as the midpoint
    first = 0
    last = len(arr) - 1
    found = False
    while first  <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == itemSearch:
            print "Found at position", mid
            return True
        elif arr[mid] > itemSearch:
            last = mid - 1
        else:
            first = mid + 1
    print "Not found"
    return False
            
    
arr = [2, 3, 5, 6, 7, 8]
binarySearch(arr, 3)            
        