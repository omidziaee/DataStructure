'''
Created on Oct 5, 2019

@author: omid
You got a list of words and a new word. The abbreviation is like the first letter the length of the letters in between the
first and the last letter plus the last letter:
l|ocalizatio|n          --> l10n
d|o|g                   --> d1g
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's 
abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
Note: if the list contains the word and no other same abbreviation exists it is true otherwise if the same abbreviation exists
and the exact word also exists return False as it is not unique.
'''
# Thefollwoing is easy but it is very slow as for each isUnique call we run an o(n) search
class ValidWordAbbr_easy(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        # make a copy of the input
        self.dictionary = [word for word in dictionary]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for elem in self.dictionary:
            if elem == word:
                continue
            # first check the length maybe it is empty
            if len(word) == len(elem):
                if word[0] == elem[0] and word[-1] == elem[-1]:
                    return False
        
        return True

# The previous solution is not good as the list is static we need to process it in the constructor
# one time and look it up in the isUnique function in o(1)
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        # the dictionary key is first_word + len_word + last_word the value of the dictionary
        # is a set contains the words with the same abbreviation.
        self.word_dict = {}
        for word in dictionary:
            if len(word) > 2:
                key = word[0] + str(len(word)) + word[-1]
            else:
                key = word
            if key in self.word_dict:
                self.word_dict[key].add(word)
            else:
                word_set = set()
                word_set.add(word)
                self.word_dict[key] = word_set

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
            key = word[0] + str(len(word)) + word[-1]
        else:
            key = word
        if key not in self.word_dict:
            return True
        # if dictionary contains the word 
        elif key in self.word_dict:
            # if the set value does not contain the word it means abbreviation is not unique
            if word not in self.word_dict[key]:
                return False
            elif word in self.word_dict[key] and len(self.word_dict[key]) > 1:
                # if set contains the word but it is the only one in the set it is like dictiobary already
                # has door and dear and we send door, in this case dear also have the same abbrevieation and
                # it should return False
                return False
        return True
            
            
            
            
            
        
# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["deer","door","cake","card"])
print obj.isUnique("cane")
        
        
        
        
        
        