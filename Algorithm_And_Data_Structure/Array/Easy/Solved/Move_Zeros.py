'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeros_not_space_efficiat(self, nums):
        non_zero_holder = []
        for indx in range(len(nums)):
            if nums[indx] != 0:
                non_zero_holder.append(nums[indx])
        for _ in range(len(nums) - len(non_zero_holder)):
            non_zero_holder.append(0)
        for indx in range(len(nums)):
            nums[indx] = non_zero_holder[indx]
        return nums
    
    def moveZeros_not_operation_efficiect(self, nums):
        location_last_non_zero = 0
        for indx in range(len(nums)):
            if nums[indx] != 0:
                nums[location_last_non_zero] = nums[indx]
                # We should add the last location by one after the replacemet otherwise, it will overwrite the last one!
                location_last_non_zero += 1
        for indx in range(location_last_non_zero, len(nums)):
            nums[indx] = 0
        return nums
    
    def moveZeros_space_operation_efficient(self, nums):
        location_last_non_zero = 0
        for indx in range(len(nums)):
            if nums[indx] != 0:
                self.swap(nums, location_last_non_zero, indx)
                location_last_non_zero += 1
        return nums
    
    def swap(self, nums, first_pointer, second_pointer):
        temp = nums[first_pointer]
        nums[first_pointer] = nums[second_pointer]
        nums[second_pointer] = temp
        return nums
    def move_zeros_simple(self, nums):
        counter_non_zero = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[counter_non_zero] = nums[index]
                counter_non_zero += 1
        nums[counter_non_zero:len(nums)] = [0] * (len(nums) - counter_non_zero)
        
        
nums = [0, 0, 1, 2, 3, 0, 4]

sol = Solution()
#print sol.moveZeros_not_space_efficiat(nums)
#print sol.moveZeros_not_operation_efficiect(nums)
print sol.moveZeros_space_operation_efficient(nums)