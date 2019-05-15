'''
Created on Jan 19, 2019

@author: omid
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
'''
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        p_split = paragraph.split(' ')
        word_count_dic = {}
        for word in p_split:
            word = [char for char in word if char.isalpha()]
            word = ''.join(word)
            if word in word_count_dic:
                word_count_dic[word] += 1
            else:
                word_count_dic[word] = 1
        max_unbanned_occurance = 0
        for word, occurance in word_count_dic.items():
            if word not in banned:
                max_unbanned_occurance = max(max_unbanned_occurance, occurance)
                if occurance == max_unbanned_occurance:
                    word_max = word
                
        return word_max
    
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
sol = Solution()
print sol.mostCommonWord(paragraph, banned)