'''
Created on Dec 30, 2018

@author: omid
'''
import unittest


def is_single_riffle_space_time_ineffieint(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    # This is a recursive approach
    # Base case
    if len(shuffled_deck) == 0:
        return True
    
    if (len(half1) > 0) and (half1[0] == shuffled_deck[0]):
        return is_single_riffle_space_time_ineffieint(half1[1:], half2, shuffled_deck[1:])
    if (len(half2) > 0) and (half2[0] == shuffled_deck[0]):
        return is_single_riffle_space_time_ineffieint(half1, half2[1:], shuffled_deck[1:])
    
    return False

def is_single_riffle(half1, half2, shuffled_deck, half1_index = 0,\
half2_index = 0, shuffled_deck_index = 0):
    if len(shuffled_deck) == shuffled_deck_index:
        return True
    if (half1_index < len(half1) and half1[half1_index] == shuffled_deck[shuffled_deck_index]):
        half1_index += 1
    elif (half2_index < len(half2) and half2[half2_index] == shuffled_deck[shuffled_deck_index]):
        half2_index += 1
    else:
        return False
    shuffled_deck_index += 1
    return is_single_riffle(half1, half2, shuffled_deck, half1_index, half2_index, shuffled_deck_index)
        


# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)