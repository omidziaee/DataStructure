'''
Created on Oct 16, 2019

@author: USOMZIA
Lexographinc means ascending
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Start from the end of the list and move backward to find the first non_decreasing point
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1 # remember the index of increase
        while nums[j] <= nums[k]:
            j -= 1
        # Now j is the index of a number greater than the one in k so they should be a swap
        temp = nums[j]
        nums[j] = nums[k]
        nums[k] = temp
        # Finally we need to reverse whatever after k
        r, l = len(nums) - 1, k + 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
         
         
nums = [1,3,2]
sol = Solution()
print sol.nextPermutation(nums)