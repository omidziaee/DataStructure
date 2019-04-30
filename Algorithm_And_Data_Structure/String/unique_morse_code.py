'''
Created on Feb 28, 2019

@author: USOMZIA
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic_alpha_morse = {"a":".-","b":"-...","c":"-.-.","d":"-..",
                           "e":".","f":"..-.","g":"--.","h":"....","i":"..",
                           "j":".---","k":"-.-","l":".-..","m":"--","n":"-.",
                           "o":"---","p":".--.","q":"--.-","r":".-.","s":"...",
                           "t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--",
                           "z":"--.."}
        
        dic_word_morse = {}   
        for word in words:
            word_morse = ""
            for char in word:
                word_morse += dic_alpha_morse[char]
            if word_morse in dic_word_morse:
                dic_word_morse[word_morse].append(word)
            else:
                dic_word_morse[word_morse] = [word]
        return dic_word_morse
    
words = ["gin", "zen", "gig", "msg"]
sol = Solution()
print sol.uniqueMorseRepresentations(words)
