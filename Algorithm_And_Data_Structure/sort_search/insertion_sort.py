'''
Created on May 29, 2019

@author: USOMZIA
https://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
Note: The advantage of insertion sort is comparing selection sort and bubble sort and merge-sort is that Insertion Sort 
runs in linear time on nearly sorted arrays.
There are two loops, the outer loop is to take the element and the original position, the inner loop is to traverse the left side
and find the position of the current element in that.
current element = 31
[17 26 54 77 93 31 44 55 20]
93 is greater than 31 so it is assumed the new position for 31 is the position of 93
[17 26 54 77    93 44 55 20]
now check 31 and 77 so 31 is less than 77 then we need to swap again
[17 26 54    77 93 44 55 20]
[17 26    54 77 93 44 55 20]
Done!!
So the stop criteria is either exhausting the array or arrive to the correct position. Bear in mind as we move forward 
left side is always sorted.
'''
class Solution():
    def insertion_sort(self, nums):
        # outer loop for traversing the array
        for i in range(1, len(nums)):
            current_value = nums[i]
            current_position = i
            # Outer loop for finding the appropriate place of the current value in the left sorted part
            while current_position > 0 and current_value < nums[current_position - 1]:
                # It is supposed that the position of current_value is i so empty nums[i]
                nums[current_position] = nums[current_position - 1]
                # So current_position should go one down
                current_position -= 1
            # Ok now either left side has exhausted or the position which current_value >= nums[i - 1] found
            nums[current_position] = current_value
        return nums
    
sol = Solution()
print sol.insertion_sort([1, 10, 4, 6, 2, 7, 9, 8])
                
                
