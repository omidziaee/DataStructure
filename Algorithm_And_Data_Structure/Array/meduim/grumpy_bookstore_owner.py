'''
Created on Sep 18, 2019

@author: USOMZIA
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers 
(customers[i]) enter the store, and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, 
otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise 
they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
'''
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        number_sure_statisfied = 0
        for i in range(len(customers)):
            if grumpy[i] != 1:
                number_sure_statisfied += customers[i]
                # as we count this satisfied customer we need to make it zero here
                customers[i] = 0
        # create the first window
        max_number_satisfied= -float('inf')
        curr_window_sum = 0
        for i in range(X):
            curr_window_sum += customers[i]
        # Now move the window 
        for i in range(X, len(customers)):
            # first update the max then update the curren window sum
            max_number_satisfied = max(curr_window_sum, max_number_satisfied)
            # update the curr_window_sum
            curr_window_sum -= customers[i - X] 
            curr_window_sum += customers[i]
        # Don't miss the last one
        max_number_satisfied = max(curr_window_sum, max_number_satisfied)   
            
            
        return max_number_satisfied + number_sure_statisfied
            
            
customers = [1,0,1,2,1,1,7,5]
grumpy    = [0,1,0,1,0,1,0,1]
X = 3
sol = Solution()
print sol.maxSatisfied(customers, grumpy, X)
            