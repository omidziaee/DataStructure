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
'''
class Solution(object):
    def merged_sorted_arrays(self, num1, num2):
        i = 0
        j = 0
        k = 0
        arr = []
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                arr[k] = num1[i]
                i += 1
            else:
                arr[k] = num2[j]
                j += 1
            k += 1
        while i < len(num1):
            arr[k] = num1[i]
            i += 1
            k += 1
        while j < len(num2):
            j += 1
            k += 1
        for k in range(len(arr)):
            num2[k] = arr[k]
        return num2
            
    def merged_sorted_to_first(self, nums1, nums2, m, n):
        # Super smart way!
        # Here as we dont want to create a new array and append into it we can instead of checking which
        # element of the arrays is smaller than the other one we can check which one is bigger! Because if
        # we check lets say the first element of the second is less than the first element of the first array
        # if it is it is ok we can insert it as the first element of the first array but of it is not we need
        # to check all the elements of the first arr one by one which ends up in two nested loop! o(m*n)
        # m is the length of nums1 without zeros at the end
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # This is for the case that if any element of nums2 remains then insert in front of nums1 as if it has remained
        # for sure it is less than the elements of nums1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1
            
            
num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]  
sol = Solution()
print sol.merged_sorted_to_first(num1, num2)    
