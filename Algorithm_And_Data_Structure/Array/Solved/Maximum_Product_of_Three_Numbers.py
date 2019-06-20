'''
Created on Sep 27, 2018

@author: USOMZIA
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

class Solution(object):
    # The idea is to find the maximum/minimum of two and max and min num then max product of three is equal to max/min product of two times either max or min num
    # whichever is bigger! Just make sure where you update the min and max! You should update these two values after whereever in pranthsis max and min
    # is
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Edge case
        if len(nums) < 3:
            raise Exception("nums should at least have three numbers!")
        # Ok inorder to do it without sorting and increasing the time to o(nlogn) we need to use brute_force. Brute_force means find the maximum possible at each iteration 
        # and update the maximum number
        # So in each iteration we need to update these three and it sould be IN-ORDER!! VERY IMPORTANT IN_ORDER
        # 1) max_product_of_three
        # 2) max_product_of_two
        # 3) min_product_of_two
        # 4) max_number
        # 5) min_number
        # Initialization
        max_num = max(nums[0], nums[1])
        min_num = min(nums[0], nums[1])
        max_product_of_two = nums[0] * nums[1]
        min_product_of_two = nums[0] * nums[1]
        max_product_of_three = nums[0] * nums[1] * nums[2]
        # It does not matter at the first iteration we compare the max_product_of_three against itself
        for index in range(2, len(nums)):
            current_num = nums[index]
            # First update the biggest contigues one
            max_product_of_three = max(max_product_of_three, max_product_of_two * current_num, min_product_of_two * current_num)
            # Second update the max_product_of_two; min_num * current_num in the case that both of them are large negative numbers
            max_product_of_two = max(max_product_of_two, max_num * current_num, min_num * current_num)
            #Third update the min_product_of_two; max_num * current_num in the case that max_num is a large positive and current_num is negative
            min_product_of_two = min(min_product_of_two, min_num * current_num, max_num * current_num)
            # Now update the max and min num
            max_num = max(max_num, current_num)
            min_num = min(min_num, current_num)
        return max_product_of_three
    
    def maximumProduct_new(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        min_1 = float('inf')
        min_2 = float('inf')
        max_1 = -float('inf')
        max_2 = -float('inf')
        max_3 = -float('inf')
        for i in range(len(nums)):
            if nums[i] < min_1:
                # order is important if first min_1 = nums[i] and then min_2 = min_1
                # then both will be nums[i]
                min_2 = min_1
                min_1 = nums[i]
            elif nums[i] < min_2:
                min_2 = nums[i]
            if nums[i] > max_1:
                # order of replacement is important 
                max_3 = max_2
                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] > max_2:
                max_3 = max_2
                max_2 = nums[i]
            elif nums[i] > max_3:
                max_3 = nums[i]
        return max(min_1 * min_2 * max_1 , max_1 * max_2 * max_3)

        
            
        
        
        
sol = Solution()
print sol.findMaxMul([-4,-3,-2,-1,60])
