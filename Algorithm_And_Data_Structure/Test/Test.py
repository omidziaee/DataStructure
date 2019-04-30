class Solution(object):
    def generateParenthesis(self, n):
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
    
sol = Solution()
print sol.generateParenthesis(5)