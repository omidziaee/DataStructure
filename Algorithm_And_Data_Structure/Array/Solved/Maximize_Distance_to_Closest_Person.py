'''
Created on Sep 27, 2018

@author: USOMZIA
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
'''
class Solution(object):
    
    def find_max_distance(self, seats):
        # We need to count the number of leading zeros and the number of 
        # trailing zeros. Also the maximum length of zeros between two ones. 
        # Basically two pointers one to keep the place of last one and one for the current
        first_one_position = 0
        last_one_position = 0
        max_distace_in_between = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                #This is for finding the position of the first one in the array!
                if seats[0] == 0 and last_one_position == 0:
                    first_one_position = i
                max_distace_in_between = max(max_distace_in_between, i - last_one_position)
                # Do not forget to update the position of the last one in the array!
                last_one_position = i
        num_of_lead_zeros = first_one_position
        num_of_trail_zeros = len(seats) - last_one_position - 1
        result = max(num_of_lead_zeros, num_of_trail_zeros, max_distace_in_between / 2)
        return result
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        first_one_position = 0
        last_one_position = 0
        max_distace_in_between = 0
        num_of_lead_zeros = 0
        num_of_trail_zeros = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if seats[0] == 0 and last_one_position == 0:
                    first_one_position = i
                max_distace_in_between = max(max_distace_in_between, i - last_one_position)
                last_one_position = i
        num_of_lead_zeros = first_one_position
        num_of_trail_zeros = len(seats) - last_one_position - 1
        return max(num_of_lead_zeros, num_of_trail_zeros, max_distace_in_between / 2)
    
    # The following also works however it is naive because after you finished the first path you again look for 
    # the first and last one in the array however it is possible like the above methods to find the first and last one
    # in just one path. 
    def find_max_distance(self, seats):
        # Todo edgecase
        temp_max = 0
        global_max = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                temp_max += 1
                global_max = max(global_max, temp_max)
            else:
                temp_max = 0
        max_distance = global_max / 2 + 1
        if seats[0] == 0:
            first = 0
            for i in range(len(seats)):
                if seats[i] == 0:
                    first += 1
                else:
                    break
            max_distance = max(max_distance, first)
        if seats[-1] == 0:
            last = len(seats) - 1
            for i in range(len(seats) - 1, -1, -1):
                if seats[i] == 0:
                    last -= 1
                else:
                    break
            max_distance = max(max_distance, len(seats) - last - 1)
        return max_distance
    
sol = Solution()
print sol.maxDistToClosest([1,0,0,1])
                
                
                
                    
                         
            
            
        
