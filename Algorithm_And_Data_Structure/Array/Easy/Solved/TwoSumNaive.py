'''
Created on Sep 4, 2018

@author: USOMZIA
This is naive solution as it has two nested loop and it is O(n^2)
'''

def twoSum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == target - arr[i]:
                result.append(i)
                result.append(j)
                
    return result


arr = [1, 2, 3, 7, 10]
target = 4
print twoSum(arr, target)