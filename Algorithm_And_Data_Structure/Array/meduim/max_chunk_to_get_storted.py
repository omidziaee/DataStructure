'''
Created on Sep 2, 2019

@author: omid
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into
some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, 
the result equals the sorted array.
What is the most number of chunks we could have made?
Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
The basic idea is to use max[] array to keep track of the max value until the current position, and compare
it to the sorted array (indexes from 0 to arr.length - 1). If the max[i] equals the element 
at index i in the sorted array, then the final count++.

Update: As @AF8EJFE pointed out, the numbers range from 0 to arr.length - 1. So there is no need to sort 
the arr, we can simply use the index for comparison. Now this solution is even more straightforward with O(n) 
time complelxity.

For example,

original: 0, 2, 1, 4, 3, 5, 7, 6
max:      0, 2, 2, 4, 4, 5, 7, 7
sorted:   0, 1, 2, 3, 4, 5, 6, 7
index:    0, 1, 2, 3, 4, 5, 6, 7
The chunks are: 0 | 2, 1 | 4, 3 | 5 | 7, 6
'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        dp_max = [0 for _ in range(len(arr))]
        dp_max[0] = arr[0]
        for i in range(1, len(arr)):
            dp_max[i] = max(dp_max[i - 1], arr[i])
        count = 0
        for i in range(len(arr)):
            if dp_max[i] == i:
                count += 1
        return count