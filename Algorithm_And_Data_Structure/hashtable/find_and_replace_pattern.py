'''
Created on Dec 15, 2019

@author: omid
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter
 x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another
 letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
Solution: We need two maps one from word to pattern and one from pattern to word lets say word is aa
and pattern is xy in this case map[a] = x = y which is not correct and we get it from the forwad map
now lets say word is xy and pattern is aa so in this case the map from pattern to word is map[a] = x = y
which is not acceptable. So we need two maps!
'''

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        if not words or not pattern:
            return []
        result = []
        for word in words:
            if self.is_good(word, pattern):
                result.append(word)
        return result
    def is_good(self, word, pattern):
        map_word, map_pattern = {}, {}
        for i in range(len(word)):
            if word[i] not in map_word:
                map_word[word[i]] = pattern[i]
            if pattern[i] not in map_pattern:
                map_pattern[pattern[i]] = word[i]
            if map_word[word[i]] != pattern[i] or map_pattern[pattern[i]] != word[i]:
                return False
        return True
    
'''
// Java solution
class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> res = new ArrayList<String>();
        for(String word: words){
            if(isGood(word, pattern)){
                res.add(word);
            }
        }
        return res;
        
    }
    public boolean isGood(String word, String pattern){
        Map<Character, Character> mapWordToPattern = new HashMap<Character, Character>();
        Map<Character, Character> mapPatternToWord = new HashMap<Character, Character>();
        for(int i = 0; i < word.length(); i++){
            char cWord = word.charAt(i);
            char pWord = pattern.charAt(i);
            if(!mapWordToPattern.containsKey(cWord)){
                mapWordToPattern.put(cWord, pWord);
            }
            if(!mapPatternToWord.containsKey(pWord)){
                mapPatternToWord.put(pWord, cWord);
            }
            if(mapPatternToWord.get(pWord) != cWord || mapWordToPattern.get(cWord) != pWord){
                return false;
            }
        }
        return true;
    }
}
'''
    
    