'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
My solution: create a hashmap that key is the elements and values are the number of occurances
'''
class Solution(object):
    def duplicate(self, arr):
        
        # Edge case
        if len(arr) < 2:
            return True
        
        #In order to get rid of key error import the collections
        import collections
        
        d = collections.defaultdict(int)
        for elem in arr:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1
        # Never ever return in a loop except you know that the occured case is wrong        
        for k in d:
            if d[k] != 1:
                return True
        return False
    
    def duplicateFaster(self, nums):
        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            else:
                seen.add(elem)
        return False
    
    def duplicateEvenFaster(self, nums):
        return len(nums) > len(set(nums))
            
# With HashMap you can find the place of the element which is duplicate
# But HashSet is faster            
sol = Solution()
print sol.duplicateEvenFaster([2,14,18,22,22])
            