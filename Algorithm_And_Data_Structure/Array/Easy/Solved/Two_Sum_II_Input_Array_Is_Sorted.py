'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
class Solution(object):
    def naive_solution(self, numbers, target):
        # This is not a good solution as we do not use the fact that the input list is ordered
        import collections
        keep_seen_index = {}
        # As it is said that all the numbers are unique we dont need to put convert the numbers to set
        for index, number in enumerate(numbers):
            if target - number in keep_seen_index:
                return [keep_seen_index[target - number] + 1, index + 1]
            else:
                keep_seen_index[number] = index
        return []
    
    def faster_solution(self, numbers, target):
        # two pointers approach
        right_pointer = len(numbers) - 1
        left_pointer = 0
        while left_pointer < right_pointer:
            if (numbers[left_pointer] + numbers[right_pointer] > target):
                right_pointer -= 1
            elif (numbers[left_pointer] + numbers[right_pointer] < target):
                left_pointer += 1
            else:
                if (numbers[left_pointer] + numbers[right_pointer] == target):
                    return [left_pointer + 1, right_pointer + 1] 
                
        return []
                   
    