'''
Created on Sep 27, 2018

@author: USOMZIA
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
'''
class Solution(object):
    def largestNum(self, nums):
        maxElem = max(nums)
        passTest = True
        if len(nums) == 1:
            return 0
        for elem in nums:
            if elem != maxElem:
                if 2 * elem > maxElem:
                    passTest = False
        return nums.index(maxElem) if passTest else -1
    
    def find_largest_twice(self, nums):
        dic_place = [float('inf') for _ in range(100)]
        for i in range(len(nums)):
            dic_place[nums[i]] = i
        counter = 1
        index = 99
        max = 0
        second_to_max = 0
        while counter < 3:
            if dic_place[index] < float('inf'):
                if counter == 1:
                    max = index
                    nums_max_index = dic_place[index]
                if counter == 2:
                    second_max = index
                counter += 1
            index -= 1
        if max >= 2 * second_max:
            return nums_max_index
        else:
            return -1
                    

sol = Solution()
print sol.largestNum([3, 6, 1, 0])