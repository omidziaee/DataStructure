'''
Created on Apr 3, 2020
@author: omidziaee
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
For a given query word, the spell checker handles two categories of spelling mistakes:
Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned 
with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, 
it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
'''
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def devowel(word):
            set_vowel = set(('a', 'e', 'i', 'o', 'u'))
            word_list = list(word)
            for i in range(len(word_list)):
                if word_list[i] in set_vowel:
                    word_list[i] = '#'
            return "".join(word_list)
            #return "".join("#" if ch in set_vowel else ch for ch in word)
                
        import collections
        dic_lower = collections.defaultdict(str)
        dic_devowel = collections.defaultdict(str)
        prefect_list = set(wordlist)
        for word in wordlist:
            word_lower = word.lower()
            word_devowel = devowel(word_lower)
            # We just need to use the first word do not update
            if word_lower not in dic_lower:
                dic_lower[word_lower] = word
            if word_devowel not in dic_devowel:
                dic_devowel[word_devowel] = word
        def solve(word):
            word_lower = word.lower()
            word_devowel = devowel(word_lower)
            if word in prefect_list:
                return word
            if word_lower in dic_lower:
                return dic_lower[word_lower]
            if word_devowel in dic_devowel:
                return dic_devowel[word_devowel]
            return ""
        return map(solve, queries)
    
    
'''
Java:
class Solution {
    Set<String> prefectSet = new HashSet<>();
    Map<String, String> mapCap = new HashMap<>();
    Map<String, String> mapDevowel = new HashMap<>();
    public String[] spellchecker(String[] wordlist, String[] queries) {
        int N = queries.length;
        String[] res = new String[N];
        for(String word: wordlist){
            String wordLower = word.toLowerCase();
            String wordDevowel = devowel(wordLower);
            if(!mapCap.containsKey(wordLower)){
                mapCap.put(wordLower, word);
            }
            if(!mapDevowel.containsKey(wordDevowel)){
                mapDevowel.put(wordDevowel, word);
            }
            prefectSet.add(word);
        }
        int i = 0;
        for(String word: queries){
            res[i++] = solve(word);
        }
        return res;
    }
    public String solve(String word){
        String ret = "";
        String wordLower = word.toLowerCase();
        String wordDevowel = devowel(wordLower);
        if(prefectSet.contains(word)){
            return word;
        }
        if(mapCap.containsKey(wordLower)){
            return mapCap.get(wordLower);
        }
        if(mapDevowel.containsKey(wordDevowel)){
            return mapDevowel.get(wordDevowel);
        }
        return ret;
    }
    public String devowel(String word){
        StringBuilder newWord = new StringBuilder();
        Set<Character> vowelSet = new HashSet<>();
        vowelSet.add('a'); 
        vowelSet.add('e'); 
        vowelSet.add('i');
        vowelSet.add('o');
        vowelSet.add('u');
        char[] wordArray = word.toCharArray();
        for(Character ch: wordArray){
            if(vowelSet.contains(ch)){
                newWord.append('#');
            } else{
                newWord.append(ch);
            }
        }
        return newWord.toString();
    }
}
'''