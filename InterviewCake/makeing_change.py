'''
Created on Jan 10, 2019

@author: USOMZIA
'''
class FindChangeWay():
    # This is the memoization map
    def __init__(self):
        self.memo = {}
        
    def change_posibilites(self, amount_left, denominations, current_index = 0):
        # The base CASE; if the amount left is zero it means that we did the job
        if amount_left == 0:
            return 1
        if current_index == len(denominations):
            return 0
        if amount_left < 0:
            return 0
        # Create the key for the memoization dictionay
        # Carefull it is not enough to have just current_index as a key_code_to_name
        # Actually as you are going to calculate the amount remaining with the current_index
        # and you want to check if you already have done for it before or not.
        # So the key is going to be a combination of amount left and the current_index
        memo_key = str((amount_left, current_index))
        # Check if we already calculate the amount_left with the current_coin
        if memo_key in self.memo:
            return self.memo[memo_key]
        current_coin = denominations[current_index]
        number_of_possible_ways = 0
        # So now we are going to check for how many times we can use the current coin
        # So each time we use 1, or two or blah blah number of coins we need to check if 
        # is possible to fit the amount_left with the other coins
        # So as far as the amount_left is greater than or equal to zero
        while amount_left >= 0:
            # We try the rest of amount with the other coins
            # and if it returns 1 which means it fits, we return one and add one to the 
            # number_of_possible_ways
            number_of_possible_ways += self.change_posibilites(amount_left, denominations, current_index + 1)
            # So we use the current coin now we need to update the amount_left
            amount_left -= current_coin
            
        self.memo[memo_key] = number_of_possible_ways
        return number_of_possible_ways
    
sol = FindChangeWay()
print sol.change_posibilites(6, [1, 2, 4])
            
        