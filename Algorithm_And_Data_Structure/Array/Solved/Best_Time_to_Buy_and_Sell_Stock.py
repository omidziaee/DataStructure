'''
Created on Sep 27, 2018

@author: USOMZIA
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution():
    def buyStockNaive(self, price):
        maxProfit = 0
        for i in range(0, len(price)):
            for j in range(i + 1, len(price)):
                profit = price[j] - price[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
    # wrong should not update min_price frist
    def buyStock(self, price):
        if len(price) == 0:
            return 0
        minPrice = price[0]
        maxProfit = 0
        for i in range(len(price)):
            if price[i] < minPrice:
                minPrice = price[i]
            else:
                profit = price[i] - minPrice
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
    
    def test_sol(self, prices):
        # In each iteration we need to check the max and min price and then update the max profit and check it with the max profit
        # edge case
        if len(prices) < 2:
            raise ValueError("At least there should be two prices!")
        
        max_price = prices[0]
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            potential_profit = price - min_price
            max_profit = max(max_profit, potential_profit)
            # You do not need this as you are not going to use it anywhere
            # There is no need to have a max_price
            max_price = max(price, max_price)
            min_price = min(price, min_price)
            
        return max_profit
    def stock_new(self, nums):
        if len(nums) <= 1:
            return 0
        max_profit = nums[1] - nums[0]
        min_price = nums[0]
        for current_time in range(1, len(nums)):
            current_price = nums[current_time]
            potential_profit = current_price - min_price
            max_profit = max(max_profit, potential_profit)
            min_price = min(min_price, current_price)
        return max_profit
            
            
            
    
sol = Solution()
print sol.stock_new([7,6,5,4])
                
        