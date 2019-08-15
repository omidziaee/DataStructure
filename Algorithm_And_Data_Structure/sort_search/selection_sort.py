'''
Created on Jul 31, 2019

@author: omid
'''
class Solution():
    def selection_sort(self, nums):
        # Two loops
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            self.swap(nums, i, min_index)
        return nums
    def swap(self, nums, i, min_index):
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
sol = Solution()
print sol.selection_sort([1, 2, 3, 8, 5, 4])