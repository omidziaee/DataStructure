'''
Created on Jan 9, 2019

@author: USOMZIA
'''
import unittest


def get_permutations(string):

    # Generate all permutations of the input string_leet_code
    #base case
    if len(string) <= 1:
        return set([string])
    perm_list = []
    for index in range(len(string)):
        head_of_perm = string[index]
        tail_of_perm = get_permutations(string[:index] + string[index + 1:])
        for perm in tail_of_perm:
            perm_list.append(head_of_perm + perm)
    
        

    return set(perm_list)



# Tests

class Test(unittest.TestCase):

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)