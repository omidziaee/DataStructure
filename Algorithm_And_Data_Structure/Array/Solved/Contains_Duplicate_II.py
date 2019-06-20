<<<<<<< HEAD
'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution(object):
    def duplicateFinder(self, nums, k):
        import collections
        d = collections.defaultdict(int)
        # Key if the dictionary is the number and value is the index of the last occurance
        for i, elem in enumerate(nums):
            if elem in d:
                if k >= i - d[elem]:
                    return True
                # The following replaces the old location with the new one as it might repeat 
                # more than twice
                else:
                    d[elem] = i
            #This is for sure for the first occurance
            else:
                d[elem] = i
        return False
    
sol = Solution()
print sol.duplicateFinder([1,0,1,1], 1)
                
=======
'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution(object):
    def duplicateFinder(self, nums, k):
        import collections
        d = collections.defaultdict(int)
        # Key if the dictionary is the number and value is the index of the last occurance
        for i, elem in enumerate(nums):
            if elem in d:
                if k >= i - d[elem]:
                    return True
                # The following replaces the old location with the new one as it might repeat 
                # more than twice
                else:
                    d[elem] = i
            #This is for sure for the first occurance
            else:
                d[elem] = i
        return False
    
sol = Solution()
print sol.duplicateFinder([1,0,1,1], 1)
                
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
            