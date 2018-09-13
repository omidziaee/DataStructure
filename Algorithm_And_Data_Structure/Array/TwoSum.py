'''
Created on Sep 4, 2018

@author: USOMZIA

'''

def twoSum(arr, target):
    # This Dic contains the key as a target - arr[key]
    # It would be very difficult and time and space colmplexity will
    # increase if the Dic keys would be the indx of the arr elements
    d = {}
    for key in range(len(arr)):
        # Check if the target - arr[key] is already exists in the dict
        if arr[key] in d:
            return [d[target - arr[key]], key]
        else:
            d[target - arr[key]] = key

arr = [3, 3, 5, 1]
target = 6
print twoSum(arr, target)