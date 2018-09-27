'''
Created on Jul 31, 2018

@author: USOMZIA
'''
def missedElem(arr1, arr2):
    seen = set()
    for elem in arr1:
        if elem in arr2:
            seen.add(elem)
        else:
            print "Missing element is " + str(elem)
    return seen
        
        
def missElemFast(arr1, arr2):
    #if len(arr1) != len(arr2):
     #   print "Two arrays are not in the same size"
     #   return False
    sum = 0
    for elem in arr1:
        sum += elem
    for elem in arr2:
        sum -= elem
    if sum != 0:
        return sum
   
missedElem([1,2,3,4,5], [1,2,3])   
print missElemFast([1,2,3,4,5], [1,2,3,4])     