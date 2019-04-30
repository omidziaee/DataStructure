'''
Created on Sep 27, 2018

@author: USOMZIA
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
My Solution: Just do the merge part of merge sort
'''
class Solution(object):
    def mergeSortedArrays(self, nums1, nums2):
        mergedArr = []
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mergedArr.append(nums1[i])
                i += 1
            else:
                mergedArr.append(nums2[j])
                j += 1
            k += 1
        while i < len(nums1):
            mergedArr.append(nums1[i])
            i += 1
            k += 1
        while j < len(nums2):
            mergedArr.append(nums2[j])
            j += 1
            k += 1
        return mergedArr
    # Copied from Leetcode
    def merge(self, nums1, m, nums2, n):
        temp1 = m-1
        temp2 = n-1
        temp3 = m+n-1

        while temp1 >= 0 and temp2 >= 0:
            if nums1[temp1] > nums2[temp2]:
                nums1[temp3] = nums1[temp1]
                temp1 -= 1
            else:
                nums1[temp3] = nums2[temp2]
                temp2 -= 1
            temp3 -= 1

        while temp2 >= 0:
            nums1[temp3] = nums2[temp2]
            temp2 -= 1
            temp3 -= 1
    
sol = Solution()
print sol.mergeSortedArrays([1,2,3,0,0,0], [2, 5, 6])
                
