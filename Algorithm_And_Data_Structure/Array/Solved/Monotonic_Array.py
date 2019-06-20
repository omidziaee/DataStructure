'''
Created on Sep 27, 2018

@author: USOMZIA
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

class Solution(object):
    def isMonotone(self, nums):
        isAsc = False
        isDesc = False
        if len(nums) <= 1:
            return True
        # When two consequtive are equal it is neither Asc nor Desc
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                isAsc = True
                if isDesc:
                    return False
            if nums[i + 1] < nums[i]:
                isDesc = True
                if isAsc:
                    return False
        return True
    def isMonotoneCount(self, nums):
        # In total the number of the comparisons is equal to the length of the array
        # Counter inc
        i = 0
        # Counter dec 
        j = 0
        for k in range(len(nums) - 1):
            if nums[k + 1] >nums[k]:
                i += 1
            elif nums[k + 1] == nums[k]:
                i += 1
                j += 1
            else:
                j += 1
        return (i == len(nums) - 1) or (j == len(nums) - 1)
    
sol = Solution()
print sol.isMonotone([1, 2, 2, 3])
                
                
                    
                    
                     
