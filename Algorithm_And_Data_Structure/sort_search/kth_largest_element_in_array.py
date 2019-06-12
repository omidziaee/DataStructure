'''
Created on Jun 4, 2019

@author: USOMZIA
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 <= k <= array's length.
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums) + 1:
            return None
        if k == len(nums) + 1:
            return max(nums)
        max_elem = max(nums)
        min_elem = min(nums)
        if min_elem < 0:
            offset = -min_elem
        elif min_elem >= 0:
            offset = 0
        bucket = [[] for _ in range(max_elem + offset + 1)]
        for i in range(len(nums)):
            bucket[nums[i] + offset].append(i)
        counter = 0
        for i in range(len(bucket) - 1, -1, -1):
            if bucket:
                counter += len(bucket[i])
            if counter >= k:
                return nums[bucket[i][0]]
        return -1
    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import _heapq
        if k > len(nums) + 1:
            return None
        if k == len(nums) + 1:
            return max(nums)
        heap_keep = []
        for i in range(len(nums)):
            _heapq.heappush(heap_keep, nums[i])
            if len(heap_keep) > k:
                _heapq.heappop(heap_keep)
        if len(heap_keep) < k:
            return -1
        return _heapq.heappop(heap_keep)
sol = Solution()
print sol.findKthLargest_1([-1, 2, 0], 1)
            
        
