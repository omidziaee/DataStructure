'''
Created on Aug 29, 2019

@author: USOMZIA
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4
'''
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The main point is we do not update the array we just calculate the movements!!!
        # As the problem stated we should just decrese the numbers to make it zig-zag
        # So in orther to change any number to make it zig zag, if the middle number is
        # greater than the neighbor numbers, we should reduce it. Therefor, we either 
        # reduce the odd numbers or even numbers. If the middle number is already less 
        # than the neighbor no need for any move. Remember at each step either odds or 
        # even can get change.
        even = odd = 0
        # You either add these two to the end or create an exception for the end elements
        nums = [float("inf")] + nums + [float("inf")]
        for i in range(1, len(nums) - 1):
            # if it is less than the minimum it is enough but we add one to it to prevent
            # the equality
            move = max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            if i % 2 == 0:
                even += move
            else:
                odd += move
        return min(odd, even)
                
            
        
    
nums = [9,6,1,6,2]
sol = Solution()
print sol.movesToMakeZigzag(nums)