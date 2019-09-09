'''
Created on Sep 5, 2019

@author: omid
Given a string s, we make queries on substrings of s.

For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right],
and then choose up to k of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the 
query is true. Otherwise, the result is false.

Return an array answer[], where answer[i] is the result of the i-th query queries[i].

Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa", 
and k = 2, we can only replace two of the letters.  (Also, note that the 
initial string s is never modified by any query.)
'''
class Solution(object):
    # This one is very slow because for each subarray we count the letters
    def canMakePaliQueries_TLE(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        list_s = list(s)
        res = []
        for query in queries:
            start, end, allow_change = query
            # For each query send it to the helper function to count as we count for each substring it is
            # very slow
            res.append(self.helper(list_s, start, end, allow_change))
        return res
    def helper(self, list_s, start, end, allow_change):
        map_chars = [0 for _ in range(26)]
        for i in range(start, end + 1):
            ch = list_s[i]
            # count the letters
            map_chars[ord(ch) - ord('a')] += 1
        odd_count = 0
        for i in range(len(map_chars)):
            if map_chars[i] % 2 != 0:
                odd_count += 1
        # Even occurances no problem as we move each one to one side the problem is for odd occurances!
        # We need to change half of the odd size lets say aaacccbb so two of them occurs odd time now if
        # we change one of the c with a then it is aaaaccbb so we need to change half of the odds but still we
        # can have one odd as we can put the odds around and the last one in the middle
        if odd_count - 2 * allow_change <= 1:
            return True
        else:
            return False
    def canMakePaliQueries_TLE2(self, s, queries):
        map_chars = [[0 for _ in range(26)] for _ in range(len(s))]
        map_chars[0][ord(s[0]) - ord('a')] = 1
        for i in range(1, len(s)):
            char = s[i]
            # You need a copy of the array either with a for loop
            # this [:] like s = copy.copy(map_chars[i-1])
            map_chars[i]= map_chars[i - 1][:]
            map_chars[i][ord(char) - ord('a')] += 1
        res_main = []
        for query in queries:
            start, end, allow_change = query
            res = []
            for i in range(26):
                if start > 0:
                    res.append(map_chars[end][i] - map_chars[start - 1][i])
                else:
                    res.append(map_chars[end][i])
            odd_counter = 0
            for i in range(len(res)):
                if res[i] % 2 != 0:
                    odd_counter += 1
            if odd_counter - 2 * allow_change <= 1:
                res_main.append(True)
            else:
                res_main.append(False)
        return res_main
    
    def canMakePaliQueries(self, s, queries):
        map_chars = [[0 for _ in range(26)] for _ in range(len(s))]
        map_chars[0][ord(s[0]) - ord('a')] = 1
        for i in range(1, len(s)):
            char = s[i]
            # You need a copy of the array either with a for loop
            # this [:] like s = copy.copy(map_chars[i-1])
            map_chars[i]= map_chars[i - 1][:]
            map_chars[i][ord(char) - ord('a')] += 1
        res_main = []
        for query in queries:
            start, end, allow_change = query
            odd_counter = 0
            for i in range(26):
                if start > 0:
                    a = map_chars[end][i] - map_chars[start - 1][i]
                    if (map_chars[end][i] - map_chars[start - 1][i]) % 2 != 0:
                        odd_counter += 1
                else:
                    if (map_chars[end][i]) % 2 != 0:
                        odd_counter += 1
            if odd_counter - 2 * allow_change <= 1:
                res_main.append(True)
            else:
                res_main.append(False)
        return res_main
    
s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
sol = Solution()
print sol.canMakePaliQueries(s, queries)
                    
        
            
        