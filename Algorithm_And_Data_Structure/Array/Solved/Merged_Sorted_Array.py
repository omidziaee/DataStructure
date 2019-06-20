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
        # element of the arrays is smaller than the other one we can check which one is bigger! 
        # Start from bigger is much easier as we do end up which easier logic
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                # If nums one has not been initialized with the zeros to the left this won't work!!!
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
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # We need two pointers to traverse over the lists and compare the values
        # We can fill the array from the begining or from the end
        # For sure it is much easier to fill it out from the end but
        # in this case it is needed to start from the max element and
        # move backward.
        pointer_to_traverse_nums1 = 0
        pointer_to_traverse_nums2 = 0
        while pointer_to_traverse_nums1 < m + n and pointer_to_traverse_nums2 < n:
            # Check the lists if the element in the second list is less than or equal to 
            # the element in the first list, the element of the second list should be inserted
            # to the first list and both pointers will increase by one. For sure do not forget to 
            # drop one zero from the end for each insert.
            if nums1[pointer_to_traverse_nums1] >= nums2[pointer_to_traverse_nums2]:
                nums1.insert(pointer_to_traverse_nums1, nums2[pointer_to_traverse_nums2])
                # Increase both itterators as we move forward on nums1
                pointer_to_traverse_nums1 += 1
                pointer_to_traverse_nums2 += 1
                # pop one zero from the end as we insert a number to the end of nums1
                #nums1.pop() # This is not necessary !!!!
            # This is an else why did you put another if here shame on you!!
            # If the element of the first list is less than the elment of the 
            else:
                pointer_to_traverse_nums1 += 1
        nums1[m + pointer_to_traverse_nums2:] = nums2[pointer_to_traverse_nums2:]
        return nums1
            
            
num1 = [1, 2, 10, 0, 0, 0, 0, 0, 0, 0]
num2 = [3, 6, 8, 12, 13, 14, 15]  
sol = Solution()
print sol.merge(num1, 3, num2, 7)    
