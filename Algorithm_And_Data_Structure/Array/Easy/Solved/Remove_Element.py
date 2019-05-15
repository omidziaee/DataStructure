<<<<<<< HEAD
'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # The idea is to use two pointers; one slow pointer and one fast pointer (same as moving zero elements to the end).
        # As far as the value of the list in the fast pointer is not equal to the defined value we replace the value in 
        # the slow pointer location with the value in the fast pointer location and increase the value of the 
        # slow pointer by one.
        pointer_to_place_nonVal = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[pointer_to_place_nonVal] = nums[index]
                pointer_to_place_nonVal += 1
        nums[pointer_to_place_nonVal:] = [None for _ in range(len(nums) - pointer_to_place_nonVal)]
        return pointer_to_place_nonVal
    
sol = Solution()
=======
'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # The idea is to use two pointers; one slow pointer and one fast pointer (same as moving zero elements to the end).
        # As far as the value of the list in the fast pointer is not equal to the defined value we replace the value in 
        # the slow pointer location with the value in the fast pointer location and increase the value of the 
        # slow pointer by one.
        pointer_to_place_nonVal = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[pointer_to_place_nonVal] = nums[index]
                pointer_to_place_nonVal += 1
        nums[pointer_to_place_nonVal:] = [None for _ in range(len(nums) - pointer_to_place_nonVal)]
        return pointer_to_place_nonVal
    
sol = Solution()
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
sol.removeElement([0,1,2,2,3,0,4,2], 2)