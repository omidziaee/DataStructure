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

arr = [4,5,2]

print checkSum(arr, 9)
print checkSumDict(arr, 9)