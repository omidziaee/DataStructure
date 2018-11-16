<<<<<<< HEAD
import unittest
=======
def reverse_words(message):
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git

<<<<<<< HEAD
def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    i = 0
    j = 0
    # It is wrong to put another counter here sorted_list[k] = my_list[i] wrong wrong you should append!!
    sorted_list = []
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            sorted_list.append(my_list[i])
            i += 1
        else:
            sorted_list.append(alices_list[j])
            j += 1
    while i < len(my_list):
        sorted_list.append(my_list[i])
        i += 1
    while j < len(alices_list):
        sorted_list.append(alices_list[j])
        j += 1
=======
    # Decode the message by reversing the words
    for i in range(len(message)):
        if message[i] != ' ':
            message.insert(len(message) - 1, message.pop(0))
        else:
            message.insert(0, messa)
            
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git
        
<<<<<<< HEAD

    return sorted_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
=======
    return message

message = list('vailt cake')
print reverse_words(message)
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git
