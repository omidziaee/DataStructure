<<<<<<< HEAD
'''
Created on Jan 19, 2019

@author: omid
'''


class Solution():
    # My idea is to create a binary_code array and fill it with one if it is capital 
    # or zero if it is lower case these two functions are usefull isupper and isalpha
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # However it says it is not empty for sure check for edgecase
        if len(word) == 0:
            return True
        binary_code = []
        for char in word:
            if char.isupper():
                binary_code.append(1)
            else:
                binary_code.append(0)
        if sum(binary_code) == len(word) or sum(binary_code) == 0:
            return True
        if sum(binary_code) == 1 and binary_code[0] == 1:
            return True
        return False
    
    # This is a nice idea man
    def detectCapitalUse_good(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        else:
            if word == word.upper() or word[1:] == word[1:].lower():
                return True
            else:
=======
'''
Created on Jan 19, 2019

@author: omid
'''


class Solution():
    # My idea is to create a binary_code array and fill it with one if it is capital 
    # or zero if it is lower case these two functions are usefull isupper and isalpha
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # However it says it is not empty for sure check for edgecase
        if len(word) == 0:
            return True
        binary_code = []
        for char in word:
            if char.isupper():
                binary_code.append(1)
            else:
                binary_code.append(0)
        if sum(binary_code) == len(word) or sum(binary_code) == 0:
            return True
        if sum(binary_code) == 1 and binary_code[0] == 1:
            return True
        return False
    
    # This is a nice idea man
    def detectCapitalUse_good(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        else:
            if word == word.upper() or word[1:] == word[1:].lower():
                return True
            else:
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
                return False