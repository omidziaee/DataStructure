'''
Created on Aug 2, 2018

@author: USOMZIA
'''
def removeDup(arr):
    a = set(arr)
    return a

def removeDuplicate(arr):
    a = []
    for elem in arr:
        if elem not in a:
            a.append(elem)
            
    return a

print removeDup([1,2,3,4,4])
print removeDuplicate([1,2,3,4,4])