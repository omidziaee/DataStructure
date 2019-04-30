class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = 1
        while len(A) < len(B):
            A += A
            q += 1
        if B in A:
            return q
        if B in A + A:
            return q + 1
        return -1
    
A = "abc"
B = "cabcabca"
sol = Solution()
print sol.repeatedStringMatch(A, B)
