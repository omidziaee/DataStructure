'''
Created on Apr 29, 2019

@author: USOMZIA
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis_whole_case(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        S = ""
        for i in range(n):
            S += "()"
        all = self.all_possible_cases(S)
        accepted = []
        for case in all:
            stack_check = []
            for char in case:
                if char == "(":
                    stack_check.append(char)
                else:
                    if stack_check:
                        stack_check.pop()
            if not stack_check:
                accepted.append(case)
        return list(set(accepted))
        
    def all_possible_cases(self, S):
        if len(S) == 1:
            return S
        result = []
        for i in range(len(S)):
            head = S[i]
            tails = self.all_possible_cases(S[:i] + S[i + 1:])
            for tail in tails:
                result.append(head + tail)
        return result
    
    def generateParenthesis_rec1(self, n):
        if not n:
            return []
        left, right = n, n
        ans = []
        self.dfs(left, right, ans, s= "")
        return ans
    def dfs(self, left, right, ans, s):
        if left == 0 and right == 0:
            ans.append(s)
        if right < left:
            return
        if left:
            self.dfs(left - 1, right, ans, s + "(")
        if right:
            self.dfs(left, right - 1, ans, s + ")")
    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        ans = []
        self.dfs_helper(0, 0, n, "", ans)
        return ans
    def dfs_helper(self, left, right, n, s, ans):
        if len(s) == 2 * n:
            return ans.append(s)
        if right > left:
            return 
        if left < n:
            self.dfs_helper(left + 1, right, n, s + "(", ans)
        if right < n:
            self.dfs_helper(left, right + 1, n, s + ")", ans)
        
            
            
sol = Solution()
print sol.generateParenthesis(3)
        
        