'''
Created on Jun 21, 2019

@author: USOMZIA
'''
class Solution():
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_num_ch = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if not digits:
            return ""
        ans = []
        current_path = []
        self.helper(digits, map_num_ch, ans, current_path, 0)
        return ans
    def helper(self, digits, map_num_ch, ans, current_path, start):
        if start == len(digits):
            return ans.append("".join(current_path))
        for ch in map_num_ch[digits[start]]:
            self.helper(digits, map_num_ch, ans, current_path + [ch] , start + 1)
        return ans
    
sol = Solution()
print sol.letterCombinations("23")
