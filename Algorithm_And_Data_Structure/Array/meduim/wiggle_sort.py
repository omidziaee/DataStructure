'''
Created on Jan 27, 2019

@author: omid
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        len_num = len(nums)
        import collections
        index = collections.deque([x for x in range(len(nums))])
        result = [None for _ in range(len(nums))]
        nums = nums + result
        for i in range(len_num):
            nums[index.popleft() + len_num] = nums[i]
            if index:
                index.append(index.popleft())
        nums = nums[len_num:]
        return nums
    def wiggle_sort_sort(self, nums):
        # the idea is first sort the array and then swap the pairs 
        # This is o(nlogn)
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            self.swap(nums, i, i + 1)
        return nums
    
    def wiggle_sort(self, nums):
        # This is o(n) so for even indices if nums[i] > nums[i + 1] we swap
        # for odd numbers if nums[i] < nums[i + 1] we swap
        even_flag = True
        for i in range(len(nums) - 1):
            if even_flag:
                if nums[i] > nums[i + 1]:
                    self.swap(nums, i , i + 1)
            else:
                if nums[i] < nums[i + 1]:
                    self.swap(nums, i, i + 1)
            # The next index is odd change the even_flag to False
            even_flag = not even_flag
        return nums  
    
    def wiggle_sort_cleaner(self, nums):
        # This is similar to the previous one just cleaner
        for i in range(len(nums) - 1):
            if ((i % 2 == 0 and nums[i] > nums[i + 1])\
                or (i % 2 == 1 and nums[i] < nums[i + 1])):
                self.swap(nums, i , i + 1)
        return nums
                     
            
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    

nums = [3,5,2,1,6,4]   
sol = Solution()
print sol.wiggle_sort_cleaner(nums)
            