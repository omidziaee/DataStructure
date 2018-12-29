'''
Created on Dec 27, 2018

@author: omid
'''

import unittest

'''
def highest_product_of_3_naive(list_of_ints):

    # Calculate the highest product of three numbers
    sorted_list_of_ints = sorted(list_of_ints)
    if sorted_list_of_ints[0] < 0:
        first_two_and_last = sorted_list_of_ints[0] * sorted_list_of_ints[1] * sorted_list_of_ints[-1]
        last_three = sorted_list_of_ints[-1] * sorted_list_of_ints[-2] * sorted_list_of_ints[-3]
        max_three = max(first_two_and_last, last_three)
    else:
        max_three = sorted_list_of_ints[-1] * sorted_list_of_ints[-2] * sorted_list_of_ints[-3]

    return max_three
'''
def highest_product_of_3(list_of_ints):
    
    # Edge case
    if len(list_of_ints) < 3:
        raise indexError("At least three numbers needed!")

    # Calculate the highest product of three numbers
    # The shortest time is o(n) as we need to check all the elements at least once
    # If you sort it then the time will be o(nlogn)!
    # At each step we need to update and check the max_product_of_tow, min_product_of_two
    # max_num and min_num. We are looking for mins as we might have negative numbers!
    min_number = min(list_of_ints[0], list_of_ints[1])
    max_number = max(list_of_ints[0], list_of_ints[1])
    
    max_product_of_two = list_of_ints[0] * list_of_ints[1]
    min_product_of_two = list_of_ints[0] * list_of_ints[1]
    
    max_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    # Start the counter from 2 as we already check the first two
    for i in range(2, len(list_of_ints)):
        # Do not update the max and min first as if the current number is the max
        # then the max_product_of_two would be current^2 which is not what we want!
        current_number = list_of_ints[i]
        
        max_product_of_three = max(max_product_of_three,\
        max_product_of_two * current_number,\
        min_product_of_two * current_number)
        
        # If both min_number and the current_number are negative max can be min*curr
        max_product_of_two = max(max_product_of_two,\
        max_number * current_number,\
        min_number * current_number)
        
        # If current_number is a big negative then max*curr can be the min product
        min_product_of_two = min(min_product_of_two,\
        min_number * current_number,\
        max_number * current_number)
        
        # Important to update min and max here!
        max_number = max(max_number, current_number)
        min_number = min(min_number, current_number)
        
    return max_product_of_three


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)