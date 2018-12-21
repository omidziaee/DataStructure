'''
Created on Dec 19, 2018

@author: USOMZIA
'''
import unittest


def is_valid(code):

    # Determine if the input code is valid
    # We need a stack to keep the parsed paranthesis and keep it!
    paran_stack = []
    # We need a dictionary to keep the open and close paran
    open_close_dic = {'[':']', '{':'}', '(':')'}
    # In order to keep the look up o(1) use set instead of array
    open_set = set(('{', '(', '['))
    #open_set = set(open_close_dic.keys())
    close_set = set(('}', ')', ']'))
    #close_set = set(open_close_dic.values())
    
    for char in code:
        if char in open_set:
            paran_stack.append(char)
        
        if char in close_set:
            # IT would be much better if you define new variable here 
            # Poping from an empty stack cause issue! So if we have extra closers that will cause issue 100%!
            # Super important to check it here! Poping from an empty stack cause issues and pops an error!
            # It is also possible to check it like this:
            # if not paran_stack:
            if paran_stack == []:
                return False
            last_open = paran_stack.pop()
            # To make sure if the stack is not empty
            if not last_open:
                return False
            # Here check if the close stack is equal to the value of the 
            if char != open_close_dic[last_open]:
                return False
    
    # Finally the stack should be empty
    return paran_stack == []
   


















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)