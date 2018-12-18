'''
Created on Nov 8, 2018

@author: USOMZIA
'''
def get_max_profit(stock_prices):

    # Calculate the max profit
    # It is not a good idea to start the max_profit with 0 as if the price goes down all the way we will have problem
    # However, initiating the max_profit with a very  low value is also not good as at the first iteration it get the value of zero
    # and remains on it forever! But if we initiate it with a very low value and start the loop to check after the first element of the
    # prices it would solve thid issue
    # We need to handle the edge case of less than two prices
    if len(stock_prices) < 2:
        raise ValueError("In order to calculate the profit at least we need two prices!")
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]
    for current_time in range(1, len(stock_prices)):
        # It is essential to calculate the max_profit before updating the min_price. Otherwise, if the prices always go down max_profit 
        # will be zero which is wrong and it should be able to return a negative value
        max_profit = max(max_profit, stock_prices[current_time] - min_price)
        # Now you can update the min_price to prevent the max_profit be always zero in the case of stock_prices monotonically decreasing
        min_price = min(min_price, stock_prices[current_time])
    return max_profit

def get_max_profit_agh(stock_prices):
    max_profit = 0
    for buy_time in range(len(stock_prices)):
        for sell_time in range(buy_time + 1, len(stock_prices)):
            max_profit = max(max_profit, stock_prices[sell_time] - stock_prices[buy_time])
    return max_profit
            


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])





unittest.main(verbosity=2)