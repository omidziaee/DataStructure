'''
Created on Jan 3, 2019

@author: USOMZIA
'''
# The following is recursive based on the algorithm on:
# http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/DynProg/knapsack2.html
import unittest


def max_duffel_bag_value(cake_tuples, weight_capacity):
    # Calculate the maximum value we can carry
    # This is recursive I think
    if weight_capacity == 0:
        return 0                                                              
    current_value_list = [0] * len(cake_tuples)
    for index in range(len(cake_tuples)):
        current_weight, current_value = cake_tuples[index]
        if current_weight == 0 and current_value != 0:
            return (float('inf'))
        if current_weight == 0 and current_value == 0:
            continue
        if weight_capacity >= current_weight:
            current_value_list[index] = current_value + max_duffel_bag_value(cake_tuples, (weight_capacity - current_weight))
        else:
            current_value_list[index] = 0
    
    return max(current_value_list)
    
            


# Tests
class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

    

    


unittest.main(verbosity=2)