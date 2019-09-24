'''
Created on Sep 27, 2018

@author: USOMZIA
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution():
    def find_best_time_to_buy_stock(self, prices):
        # The idea is to find the back to back valleys and peaks and sum up the profits together
        peak = prices[0]
        valley = prices[0]
        max_profit = 0
        i = 0
        # Here it goes to len - 1 because the other while goes to i + 1
        while i < len(prices) - 1:
            # Here it should check i again as it can go beyond the end of the array
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i] 
            max_profit += peak - valley
        return max_profit
    
    
    def find_best_time_to_trade_optimal(self, prices):
        # Whenever we have profit we should trade to earn money that is the idea!
        max_profit = 0
        for i in range(1, len(prices)):
            # check if there is a profit because of the trading
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
    def find_best_time_to_trade_optimal_dp(self, prices):
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][0] = -prices[0]
        dp[0][1] = -float('inf')
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1] - prices[i], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[-1])
                
    
sol = Solution()
print sol.find_best_time_to_buy_stock([7, 1, 5, 3, 6, 4])
print sol.find_best_time_to_trade_optimal([7, 1, 5, 3, 6, 4])
print sol.find_best_time_to_trade_optimal_dp([7, 1, 5, 3, 6, 4])


