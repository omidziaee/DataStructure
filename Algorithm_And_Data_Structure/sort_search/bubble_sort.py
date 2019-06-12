'''
Created on May 29, 2019

@author: USOMZIA
https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html
The outer loop starts from the end and move backward as we want to place the maximum to the end
The inner loop starts from the start point and goes to the end of outer loop
First round bring the max of all the array to the last position
Second round bring the max of all the array except the last on to the last of the subarray
...
it is an o(n^2) algorithm
'''
class Solution():
    def bubble_sort(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            # It should be i + 1 because i is the last iter and i will equal to len(nums) - 1
            for j in range(1, i + 1):
                # like a bubble bring the maximum to the top
                if nums[j - 1] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
        return nums
sol = Solution()
print sol.bubble_sort([1, 10, 4, 6, 2, 7, 9, 8])