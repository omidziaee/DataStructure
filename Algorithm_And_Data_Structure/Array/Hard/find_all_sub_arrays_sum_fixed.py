'''
Created on Feb 5, 2019

@author: omid
Find all the sub arrays that sum up to the same value in almost linear time
'''
def find_sum_k(nums, k):
    # lets say we arrive to sum 5 again if we move forward and arrive to 5 again
    # it means that the sum of numbers between these two indices is zero.
    # hash-map to keep the sum and the index that sum happens there
    d = {}
    sum = 0
    # Initialize the hash-map
    # We need this to keep the place of first zero sum
    # This is for the case that from index zero to n is k
    d[0] = [-1]
    # list to keep the index of the subsets
    result = []
    for i in range(len(nums)):
        sum += nums[i]
        # For sure the indices in d[sum] are in a row as lets say we arrive to sum = 3
        # Then again if the sum would be 3 for sure there are sum positive and negative 
        # numbers in between but they are in row
        if sum in d:
            d[sum].append(i)
        else:
            d[sum] = [i]
    # ins
    for sum in d:
        if sum - k in d:
            for index in range(len(d[sum])):
                #result.append((d[sum - k][0] + 1, d[sum][index]))
                result.append(nums[d[sum - k][0]+1: d[sum][index]+1])
                
    return result
    
                

nums = [-2, 2, 3, -4, 2, 2, 2, 1]
print find_sum_k(nums, 5)
