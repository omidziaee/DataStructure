'''
Created on Oct 8, 2019

@author: omid
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest 
transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections
        def dfs(graph, end_word, begin_word):
            import collections
            keep_deque = collections.deque()
<<<<<<< HEAD
=======
            # start level from zero
>>>>>>> branch 'master' of https://github.com/omidziaee/DataStructure.git
            keep_deque.append((begin_word, 0))
            already_seen = {beginWord: True} 
            while keep_deque:
                node, level = keep_deque.popleft()
                if node == end_word:
                    return level + 1
                for i in range(len(node)):
                    key = node[:i] + "_" + node[i + 1:]
                    for neighbor in graph[key]:
                        if neighbor not in already_seen:
                            keep_deque.append((neighbor, level + 1))
                            already_seen[neighbor] = True
            return 0
                
            
        if not endWord or not wordList:
            return 0
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "_" + word[i + 1:]
                graph[key].append(word)
                
        return dfs(graph, endWord, beginWord)
    

sol = Solution()
print sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])







