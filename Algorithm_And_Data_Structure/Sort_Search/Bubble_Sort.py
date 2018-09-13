'''
Created on Jul 19, 2018

@author: USOMZIA
'''
def bubleSort(arr):
    i = 0
    j = 0
    if len(arr) == 1:
        return arr
    else:
        # It needs len(arr)-1 pass to sort all the values lets say it has 3 recordes
        # it needs 2 pass
        for i in range(len(arr) - 1):
            # you can put len(arr)-1 as well but it is not efficient so 
            # after each pass finished the last element resides in the corrct position
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    
    return arr

arr = [45,26,70,2,1]

print (bubleSort(arr))

