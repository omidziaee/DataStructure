'''
Created on Jul 18, 2018

@author: USOMZIA
'''
def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
            
#arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
arr = [1, 5, 3, 7, 8, 4]
merge_sort(arr)
print arr
