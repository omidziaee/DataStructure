'''
Created on Sep 27, 2018

@author: USOMZIA
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

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
            
    
sol = Solution()
print sol.buyStock([7,1,5,3,6,4])
                
        