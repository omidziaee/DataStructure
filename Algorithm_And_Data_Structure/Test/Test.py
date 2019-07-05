class Solution(object):
    def __init__(self):
        self.memo = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = []
        current_path = []
        self.unique_path_helper(m, n, ans, current_path)
        return len(ans)
    def unique_path_helper(self, m, n, ans, current_path):
        if (m, n) in self.memo:
            print "this is taken from memory %s, %s" %(str((m, n)), str(self.memo[(m, n)]))
            return self.memo[(m, n)]
        if m == 1 and n == 1:
            return ans.append(current_path)
        elif m < 1 or n < 1:
            return []
#         elif i == m - 1 and j < n - 1:
#             self.unique_path_helper(m, n, ans, current_path + ['Down'], i, j + 1)
#         elif i < m - 1 and j == n - 1:
#             self.unique_path_helper(m, n, ans, current_path + ['Right'], i + 1, j)
        self.unique_path_helper(m , n - 1, ans, current_path + ['up'])
        self.unique_path_helper(m - 1, n, ans, current_path + ['left'])
        self.memo[(m, n)] = ans
        print ans
        return ans
    
    def uniquePaths_new(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        # m and n are length not index
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        res = self.uniquePaths_new(m - 1, n) + self.uniquePaths_new(m, n - 1)
        self.memo[(m, n)] = res
        print self.memo
        return res
    
sol = Solution()
print sol.uniquePaths(3, 2)