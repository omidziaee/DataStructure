'''
Created on Jul 31, 2018

@author: USOMZIA
'''

def naiveDup(arr):
    dup = set()
    for i in range(len(arr)):
        for j in range(1+i, len(arr)):
            if arr[i] == arr[j]:
                dup.add(arr[i])
    return dup


def dup(arr):
    dupArr = []
    for elem in arr:
        if elem not in dupArr:
            dupArr.append(elem)
        else:
            print "This is a duplicate Eelem " + str(elem)
            return False

arr = [1,5,1,3]
print naiveDup(arr)
dup(arr)
                
            