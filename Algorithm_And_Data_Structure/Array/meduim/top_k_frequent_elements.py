'''
Created on Feb 7, 2019

@author: omid
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
The idea is to create a dictionary to count the occurance of each number in the array
then sort this counts with bucket sort as we know the limit of upper bound of the occurances
'''
class Solution():
    def topKFrequent(self, nums, k):
        # Todo: edge case
        if len(nums) <= k:
            return nums
        # It is not possible to have more most frequent items than the length of the array
        if k > len(nums):
            return []
        dic_count_num = {}
        for num in nums:
            if num in dic_count_num:
                dic_count_num[num] += 1
            else:
                dic_count_num[num] = 1
        # bucket is a list for sorting the dictionary or another list; for example
        # [1, 2, 2, 3, 1, 1, 1, 4]  the bucket is a list with the same length of this
        # [0, 0, 0, 0, 0, 0, 0, 0] you can initialize it or not
        # bucket = [[3, 4], [2], 0, [1], 0, 0, 0] now we know 3 and 4 occurs one time 2 occures 2 times 
        # all from the index
        bucket = [[] for _ in range(len(nums))]
        for key, value in dic_count_num.items():
            bucket[value - 1].append(key)
        
        result = []  
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) != 0:
                if len(result) < k:
                    result += bucket[i]
                else:
                    break            
        return result
    
sol = Solution()
print sol.topKFrequent([4,1,-1,2,-1,2,3], 2)
                
                