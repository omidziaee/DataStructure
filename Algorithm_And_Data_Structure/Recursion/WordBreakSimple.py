'''
Created on Aug 21, 2018

@author: USOMZIA
'''

# This is good for splitting the string in just two words
# So first search the prefix (First section of the string) and 
# following that search the rest of the string in the dict
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    for i in range(1, len(s)):
        prefix = s[0: i]
        if prefix in wordSet:
            for j in range(i, len(s)):
                postFix = s[j:]
                if postFix in wordSet:
                    return True
    return False
            
 

print wordBreak("leetcode", ["leet", "code", "pen"])
                