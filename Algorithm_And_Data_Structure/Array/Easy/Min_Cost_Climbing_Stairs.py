<<<<<<< HEAD
'''
Created on Sep 27, 2018

@author: USOMZIA
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Base case
        if len(cost) <= 2:
            return 0
        cost_from_stair = [0 for _ in range(len(cost))]
        for i in range(len(cost) - 1):
            cost_from_stair[i] = cost[i] + min(self.minCostClimbingStairs(cost[i+1:]),\
                                               self.minCostClimbingStairs(cost[i+2:]))
        return cost_from_stair
            
sol = Solution()
=======
'''
Created on Sep 27, 2018

@author: USOMZIA
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Base case
        if len(cost) <= 2:
            return 0
        cost_from_stair = [0 for _ in range(len(cost))]
        for i in range(len(cost) - 1):
            cost_from_stair[i] = cost[i] + min(self.minCostClimbingStairs(cost[i+1:]),\
                                               self.minCostClimbingStairs(cost[i+2:]))
        return cost_from_stair
            
sol = Solution()
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print sol.minCostClimbingStairs([0, 1, 1])