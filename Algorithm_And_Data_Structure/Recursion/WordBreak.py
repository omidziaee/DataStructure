'''
Created on Aug 21, 2018

@author: USOMZIA
'''

# This is very similar to the simplified version the only difference is 
# here after we find the prefix, the rest of the string_leet_code goes to a recursive
# process as for sure there is more than just one postfix!
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    for i in range(1, len(s)):
        prefix = s[0:i]
        if prefix in wordSet:
            return recWordBreak(s[i:], wordSet, False)
    return False
            
     
def recWordBreak(s, wordSet, isFinished): 
    #base case
    if isFinished:
        return True      
    for j in range(1, len(s)+1):
        postfix = s[0:j]
        if postfix in wordSet:
            return recWordBreak(s[j:], wordSet, j == len(s))
                
    return False

print wordBreak("leetcodecodepen", ["leet", "code", "pen"])
                