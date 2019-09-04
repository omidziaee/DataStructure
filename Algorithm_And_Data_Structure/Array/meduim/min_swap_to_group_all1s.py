'''
Created on Sep 2, 2019

@author: omid
Given a binary array data, return the minimum number of swaps required to group all 1s present in the array together
in any place in the array.
Example 1:
Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:
Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
Example 3:
Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
'''
class Solution(object):
    def minSwaps_slow(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        one_counter = 0 # sum(data)
        for i in range(len(data)):
            if data[i] == 1:
                one_counter += 1
        if one_counter == len(data) or len(data) == 0:
            return 0
        # create a window with left and right ends
        l, r = 0, one_counter
        # Now we want to find the windows with the length of one_counter that has the 
        # most ones
        max_ones_in_window = 0
        while r < len(data):
            number_of_ones_window = 0
            # This one is slow because each time you sum from start again
            for i in range(l, r):
                number_of_ones_window += data[i]
            max_ones_in_window = max(max_ones_in_window, number_of_ones_window)
            l += 1
            r += 1
        return one_counter - max_ones_in_window
    
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        #one_counter = 0 # sum(data)
        # for i in range(len(data)):
        #     if data[i] == 1:
        #         one_counter += 1
        one_counter = sum(data)
        if one_counter == len(data) or len(data) == 0:
            return 0
        # create a window with left and right ends
        l, r = 0, one_counter
        # Now we want to find the windows with the length of one_counter that has the 
        # most one
        max_ones_in_window = -float("inf")
        curr_sum = sum(data[l: r])
        while r < len(data):
            max_ones_in_window = max(max_ones_in_window, curr_sum)
            curr_sum = curr_sum + data[r] - data[l]
            l += 1
            r += 1
        return one_counter - max_ones_in_window 
            
with open("input.csv", "r") as f:
    data = list(f.read().split(","))
ans = []
for i in range(len(data)):
    ans.append(int(data[i]))
print ans
#ans = [1,0,1,0,1,0,0,1,1,0,1]               
sol = Solution()
print sol.minSwaps(ans)
    