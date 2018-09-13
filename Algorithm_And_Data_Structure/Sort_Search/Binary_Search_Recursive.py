'''
Created on Jul 19, 2018

@author: USOMZIA
'''
# Binary search with recursion
def recBinarySearch(arr, item):
    # Base case for recursion
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == item:
            return True
        elif arr[mid] > item:
            arr = arr[:mid + 1]
            return recBinarySearch(arr, item)
        elif arr[mid] < item:
            arr = arr[:mid]
            return recBinarySearch(arr, item)


arr = [1, 2, 3, 4, 5]
print recBinarySearch(arr, 2)