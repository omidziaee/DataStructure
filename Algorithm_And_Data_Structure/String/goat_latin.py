'''
Created on Jan 19, 2019

@author: omid
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # go over the string in one pass just keep in mind string is immutable but
        # you can concatinate strings together
        str_result = ''
        S_list = S.split(' ')
        # In order to make it o(1) search it can either be set or dictionary
        vowels = set(['a', 'i', 'o', 'e', 'u', 'A', 'I', 'O', 'E', 'U'])
        for i, word in enumerate(S_list):
            word_list = list(word)
            if word_list[0] in vowels:
                word_list.append('ma')
                word = ''.join(word_list)
                str_result += word
            else:
                word_list.append(word_list.pop(0))
                word_list.append('ma')
                word = ''.join(word_list)
                str_result += word
            str_result += 'a' * (i + 1) + ' '
        # You can manipulate the whole string but not the element by element! String is immutable
        str_result = str_result[:-1]
        return str_result
    def toGoatLatin_cleaner(self, S):
        str_result = ''
        S_list = S.split(' ')
        # In order to make it o(1) search it can either be set or dictionary
        vowels = set(['a', 'i', 'o', 'e', 'u', 'A', 'I', 'O', 'E', 'U'])
        for i, word in enumerate(S_list):
            word_list = list(word)
            if word_list[0] not in vowels:
                word_list.append(word_list.pop(0))
                word = ''.join(word_list)
                str_result += word
            # You still need to check for the case that if the first element is not a vowel
            # In this case just add it to the string!
            else:
                word = ''.join(word_list)
                str_result += word
            str_result += 'ma' + 'a' * (i + 1) + ' '
        # You can manipulate the whole string but not the element by element! String is immutable
        str_result = str_result[:-1]
        return str_result
        
S = "I speak Goat Latin"    
sol = Solution()
print sol.toGoatLatin(S)
            
        
