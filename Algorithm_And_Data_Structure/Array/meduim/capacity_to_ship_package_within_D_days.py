'''
Created on Sep 9, 2019

@author: USOMZIA
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the
ship with packages on the conveyor belt (in the order given by weights). We may not load 
more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the 
conveyor belt being shipped within D days.
Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
'''
class Solution():
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        # The minimum weight is when the container can convey the max of the weights. But in this case the number
        # of days is maximum. On the other hand, if the container can convey the sum of the weights it can transfer 
        # all of it in one day. So we have a search space for the weight between maximum of weights and sum of the 
        # weights.
        left = max(weights)
        right = sum(weights)
        # We need to do a binary search in this space 
        while left < right:
            mid = left + (right - left) / 2
            curr_weight = 0
            day_so_far = 1
            for weight in weights:
                curr_weight += weight
                # Check if the curr_weight is bigger than the mid
                if curr_weight > mid:
                    curr_weight = weight
                    day_so_far += 1
            if day_so_far <= D:
                # this means that we put more stuff in the container and we can make it lighter but spread in more
                # day as we still does not reach D days.
                right = mid # The reason it is not mid - 1 is we already put curr_weight > mid so here it should be mid
            else:
                left = mid + 1
        return left
        
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
sol = Solution()
print sol.shipWithinDays(weights, D)







