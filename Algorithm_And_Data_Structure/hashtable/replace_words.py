'''
Created on Oct 22, 2019

@author: USOMZIA
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's 
call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence 
with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
'''
class Solution():
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if len(sentence) == 0 or not dict:
            return sentence
        dict_set = set(dict)
        def word_find(word):
            for i in range(1, len(word)):
                if word[:i] in dict_set:
                    return word[:i]
            return word
        return " ".join(map(word_find, sentence.split(" ")))
        
        
dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print sol.replaceWords(dict, sentence)