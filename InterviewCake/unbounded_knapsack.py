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
    current_value_list_plus_current_value = [0] * len(cake_tuples)
    for index in range(len(cake_tuples)):
        current_weight, current_value = cake_tuples[index]
        if weight_capacity >= current_weight:
            current_value_list[index] = max_duffel_bag_value(cake_tuples, (weight_capacity - current_weight))
        else:
            current_value_list[index] = 0
    for index in range(len(cake_tuples)):
        current_weight, current_value = cake_tuples[index]
        if weight_capacity >= current_weight:
            current_value_list_plus_current_value[index] = current_value_list[index] + current_value
        else:
            current_value_list_plus_current_value[index] = 0
    return max(current_value_list_plus_current_value)
    
            


# Tests

class Test(unittest.TestCase):

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (2,4), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 14
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)