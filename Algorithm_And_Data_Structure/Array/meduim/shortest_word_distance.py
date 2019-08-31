'''
Created on Aug 27, 2019

@author: USOMZIA
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = "makes", word2 = "coding"
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # This is a two pointer problem one pointer for word1 and the other for word2
        p_word1 = -float("inf")
        p_word2 = float("inf")
        # We need to handle the equal case somehow otherwise it is easy
        is_same = word1 == word2
        min_distance = float("inf")
        for i, word in enumerate(words):
            if word == word1:
                # just this part is different than the non-repeated version
                # if the wrods are repeated it always stay in the same if word == word1
                # Therefore we need to swap the values of the two pointers!!
                if is_same:
                    p_word1 = p_word2
                    p_word2 = i
                else:
                    p_word1 = i
            elif word == word2:
                p_word2 = i
            min_distance = min(min_distance, abs(p_word2 - p_word1))
        return min_distance
            
                
            
        
    
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
sol = Solution()
print sol.shortestWordDistance(words, word1, word2)
            
                
                