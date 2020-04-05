'''
Created on Dec 24, 2019

@author: omid
'''
class Solution():
    def find_longest_prefix(self, strs):
        if not strs:
            return ""
        shortest_str = min(strs, key = lambda x:len(x))
        for i in range(len(shortest_str)):
            for j in range(len(strs)):
                if shortest_str[i] != strs[j][i]:
                    return shortest_str[:i]
        return shortest_str
    
sol = Solution()
print sol.find_longest_prefix(["flow", "flong", "flight"])
                
