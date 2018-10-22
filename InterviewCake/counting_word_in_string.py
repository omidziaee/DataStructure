'''
Created on Nov 8, 2018

@author: USOMZIA

You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary, where the 
keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

  'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'
What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with 
a value of 22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
'''
def create_the_dic(the_str):
    import collections
    d = collections.defaultdict()
    # Call the helper function
    words = split_words(the_str)
    for word in words:
        if word.lower() in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
    
    

def split_words(the_str):
    # The array to keep the words
    words = []
    start_of_the_word = 0
    length_of_the_word = 0
    for i, char in enumerate(the_str):
        # you need to take care of the last word as it might not end with a punctuation or space 
        # In this case the last word will be skipped!
        if i == len(the_str) - 1:
            if char.isalpha():
                length_of_the_word += 1
                word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
                words.append(word)
            else:
                word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
                words.append(word)
        elif char.isalpha():
            if length_of_the_word == 0:
                start_of_the_word = i
            length_of_the_word += 1
        else:
            word = the_str[start_of_the_word: start_of_the_word + length_of_the_word]
            words.append(word)
            length_of_the_word = 0
    return words

print create_the_dic("this: is: omid. omid")