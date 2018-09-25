'''
Created on Sep 5, 2018

@author: USOMZIA
'''
class Solution(object):
    def binarySearch(self, arr, target):
        # base case
        if len(arr) == 0:
            print "can not find the value"
            return False
        mid = len(arr) / 2
        leftSide = arr[:mid]
        rightSide = arr[mid:]
        if target < arr[mid]:
            return self.binarySearch(leftSide, target)
        elif target > arr[mid]:
            return self.binarySearch(rightSide, target)
        elif target == arr[mid]:
            return mid
        
sol = Solution()
print sol.binarySearch([5,7,8,10], 2)
        
