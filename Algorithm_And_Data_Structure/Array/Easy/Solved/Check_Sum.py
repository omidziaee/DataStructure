'''
Created on Jul 30, 2018

@author: USOMZIA
'''
def checkSum(arr, target):
    a = set()
    for i in arr:
        if (target - i) in arr:
            a.add(target-i)
    return a


def checkSumDict(arr, target):
    a = {}
    for elem in arr:
        if (target - elem) in arr:
            a[elem] = target - elem
    return a

arr = [3,5,2]

print checkSum(arr, 6)
print checkSumDict(arr, 6)