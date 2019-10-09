'''
Created on Oct 4, 2019

@author: USOMZIA
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one 
letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 
is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
'''
class Solution():
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import collections
        if len(words) < 2:
            return len(words)
        max_chain = 0
        words.sort(key = lambda w:len(w))
        for i in range(len(words)):
            first_counter = collections.Counter(words[i])
            counter = 1
            for j in range(i + 1, len(words)):
                counter_chars = 0
                for key in first_counter.keys():
                    if key in collections.Counter(words[j]):
                        counter_chars += 1
                if counter_chars == len(first_counter):
                    counter += 1
                    first_counter = collections.Counter(words[j])
            max_chain = max(max_chain, counter)
        return max_chain 
                
words = ["ddgpj","oopwqq","ooq","oopq","iwdkeoqqtd","iwdkeoqqt","oopwq","t","wdoqqt","vcw","ddgpjy","ddpj","njpci","njci","ft","q","wdkeoqqt","dqq","qq","ni","eihk","ebiihzke","eihzke","eik","eiihzke","dqqt","eihzk","vw","ddp","oq","wdeoqqt","nci","doqqt","vft"]
sol = Solution();
print sol.longestStrChain(words)
                