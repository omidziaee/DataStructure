'''
Created on Jan 23, 2019

@author: USOMZIA
'''
class Solution(object):
    def __init__(self):
        from collections import deque
        self.dic_word_counter = {}
        self.non_repeated_queue = deque()
        
    def set(self, word):
        if word in self.dic_word_counter:
            self.dic_word_counter[word] += 1
        else:
            self.dic_word_counter[word] = 1
        if self.dic_word_counter[word] == 1:
            self.non_repeated_queue.appendleft(word)
        else:
            self.non_repeated_queue.pop()
            
        
    def get(self):
        return self.non_repeated_queue[-1]
    
sol = Solution()
sol.set("cat")
print sol.get()
sol.set("dog")
print sol.get()
sol.set("dog")
print sol.get()
sol.set("toy")
print sol.get()