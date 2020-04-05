'''
Created on Feb 23, 2020

@author: omid
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one 
character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:

You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are 
persisted across multiple test cases. Please see here for more details.
'''
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.dic = collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            self.dic[len(word)].append(word)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.dic:
            return False
        for candidate in self.dic[len(word)]:
            counter = 0
            for i, ch in enumerate(candidate):
                if ch != word[i]:
                    counter += 1
            if counter == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)











'''
Java:
class MagicDictionary {
    Map<Integer, List<String>> dic;

    /** Initialize your data structure here. */
    public MagicDictionary() {
        dic = new HashMap<>();
    }
    
    /** Build a dictionary through a list of words */
    public void buildDict(String[] dict) {
        for(String word: dict){
            int len = word.length();
            if(!dic.containsKey(len)){
                dic.put(len, new ArrayList<String>());
            }
            dic.get(len).add(word);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    public boolean search(String word) {
        int len = word.length();
        if (!dic.containsKey(len)) {
            return false;
        }
        for (String s : dic.get(len)) {
            int count = 0;
            for (int i = 0; i < len; ++i) {
                if (word.charAt(i) != s.charAt(i)) {
                    ++count;
                }
            }
            if (count == 1) {
                return true;
            }
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * boolean param_2 = obj.search(word);
 */