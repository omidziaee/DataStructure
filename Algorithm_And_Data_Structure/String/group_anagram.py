'''
Created on Jun 24, 2019

@author: USOMZIA
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution():
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype:
        """
        # Create a list of dictionaries
        dic_strs = {}
        res = []
        for str in strs:
            str_sort = ''.join(sorted(str))
            if str_sort in dic_strs:
                dic_strs[str_sort].append(str)
            else:
                dic_strs[str_sort] = [str]
        for value in dic_strs.values():
            res.append(value)
        return res
    def groupAnagrams_best(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for s in strs:
            # For each string we need to create this count
            count = [0 for _ in range(26)]
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            # Important: it should be tuple! list can not be used as a key!!
            if tuple(count) in ans:
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]
        return ans.values()
sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    
                
        