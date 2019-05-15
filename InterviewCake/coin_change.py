'''
Created on Dec 12, 2018

@author: USOMZIA
'''
import unittest

'''
def change_possibilities(amount, denominations, current_index = 0):

    # Calculate the number of ways to make change
    # base case
    if amount == 0:
        return 1
    
    if amount < 0:
        return 0
        
    if current_index == len(denominations):
        return 0
    
    print "Finding the number of possible %i amount with coins %s" %(amount, denominations[current_index:])
    
    current_coin = denominations[current_index]
    
    possible_number = 0
    
    while amount >= 0:
        possible_number += change_possibilities(amount, denominations, current_index + 1)
        amount -= current_coin
        
    return possible_number
'''

class FindChange(object):
    def __init__(self):
        self.memo = {}
        
    def change_possibilities(self, amount_left, denominations, current_index = 0):
        
        # check if the current instance is already in the memoization dictionary
        memo_key = str((amount_left, current_index))
        
        if memo_key in self.memo:
            print  "grabbing memo[%s]" %memo_key
            return self.memo[memo_key]
         
        if amount_left == 0:
            return 1
            
        if amount_left < 0:
            return 0
            
        if current_index == len(denominations):
            return 0
        
        current_coin = denominations[current_index] 
        possible_num = 0
        
        while amount_left >= 0:
            possible_num += self.change_possibilities(amount_left, denominations, current_index + 1)
            amount_left -= current_coin
            
        self.memo[memo_key] = possible_num
        print self.memo
        return possible_num





# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)
'''
    def test_one_way_to_make_zero_cents(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        find_change = FindChange()
        actual = find_change.change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)
'''

unittest.main(verbosity=2)