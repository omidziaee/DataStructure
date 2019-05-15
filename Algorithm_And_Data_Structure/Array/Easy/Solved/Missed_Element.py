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
    
def miss_elem_faster(arr1, arr2):
    import collections
    d = collections.defaultdict()
    missed_elems = []
    for number in arr1:
        if number in d:
            d[number] += 1
        else:
            d[number] = 1
    for num in arr2:
        if num in d:
            d[num] -= 1
        else:
            d[num] = 1
    for key in d:
        if d[key] != 0:
            missed_elems.append(key)
    return missed_elems
            
        
        
     
print miss_elem_faster([1,2,3,4,5,6], [1,2,3,4,7])     