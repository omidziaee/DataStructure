'''
Created on Sep 27, 2018

@author: USOMZIA
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

class Solution(object):
    def remove_duplicates(self, nums):
        # Whenever there is an in place manipulation of an array, the first guess is to use two pointers
        # one slow pointer and another fast pointer. As far as the value in the fast pointer is equal to the 
        # desired value we need to just move the fast pointer and skip the slow pointer. As soon as it has passed
        # we copy the value in the fast pointer to the value in the place of slow pointer + 1
        #if len(nums) < 2:
        #   raise indexError("nums should at least have one value!")
        # Two pointer again one is fast and the other one is slow. Most of the in place modificaions can be done with
        # two pointers!
        # Slow pointer
        pointer_to_place_non_repeated = 0
        value_to_check = None
        for index in range(len(nums)):
            if nums[index] != value_to_check:
                nums[pointer_to_place_non_repeated] = nums[index]
                pointer_to_place_non_repeated += 1
                value_to_check = nums[index]
        nums[pointer_to_place_non_repeated:] = [None for _ in range(len(nums) - pointer_to_place_non_repeated)] 
        return pointer_to_place_non_repeated
    
    def remove_duplicates_easier(self, nums):
        # Fast pointer move faster to skip the repeated values
        if len(nums) == 0:
            return 0
        slow_pointer = 0
        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
        nums[slow_pointer + 1:] = [None for _ in range(len(nums) - slow_pointer)]
        return slow_pointer + 1
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # relocate the last non_repeated element to the last non_repeated index similar to move zeros problem!!
        last_unrepeated_place = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                last_unrepeated_place += 1
                nums[last_unrepeated_place] = nums[i]
        for i in range(last_unrepeated_place + 1, len(nums)):
            nums.pop()
        return len(nums)
    
sol = Solution()
print sol.remove_duplicates_easier([1, 1, 2])
