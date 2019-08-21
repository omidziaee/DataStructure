'''
Created on Aug 19, 2019

@author: USOMZIA
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements 
that don't appear in arr2 should be placed at the end of arr1 in ascending order.
Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
'''
class Solution():
    def relativeSortArray_1(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1.sort()
        dic_index = {}
        for i, elem in enumerate(arr2):
            # Unique elements
            dic_index[elem] = i
        #arr1.sort(key=lambda x:dic_index.get(x, len(arr1) + 1000))
        # 1000 is the offset number which results in moving the elements to the end
        arr1.sort(key=lambda x:dic_index[x] if x in dic_index else len(arr1) + 1000)
        return arr1
    
    def relativeSortArray(self, arr1, arr2):
        res = []
        diff = []
        dic_index = {}
        for elem in arr2:
            dic_index[elem] = 0
        for elem in arr1:
            if elem in dic_index:
                dic_index[elem] += 1
            else:
                diff.append(elem)
        for elem in arr2:
            res.extend([elem] * dic_index[elem])
        # should do it separately it is not possible to do it like res += diff.sort()
        diff.sort()
        res += diff
        return res
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sol = Solution()
print sol.relativeSortArray(arr1, arr2)
