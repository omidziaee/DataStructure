'''
Created on Jun 18, 2019

@author: USOMZIA
'''
class Solution(object):
    def __init__(self):
        # Dude for a two dimension thing in ordre to keep it you need two dimention thing
        # Recuresive pluse memoization is DP
        self.memo = {}
    def uniquePaths_old(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = []
        current_path = []
        self.unique_path_helper(m, n, ans, current_path, (0, 0), (m - 1, n - 1))
        return len(ans)
    def unique_path_helper(self, m, n, ans, current_path, i, j):
        if (i, j) in self.memo:
            print "this is already calculated %s" %str(self.memo[(i, j)])
            return self.memo[(i, j)]
        if i == m and j == n:
            print current_path
            return ans.append(current_path)
        elif i > m or j > n:
            return []
        elif i == m and j < n:
            self.unique_path_helper(m, n, ans, current_path + ['Down'], i, j + 1)
        elif i < m and j == n:
            self.unique_path_helper(m, n, ans, current_path + ['Right'], i + 1, j)
        elif i < m and j < n:
            self.unique_path_helper(m, n, ans, current_path + ['Down'], i, j + 1)
            self.unique_path_helper(m, n, ans, current_path + ['Right'], i + 1, j)
        self.memo[(i, j)] = current_path
        return ans
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        res = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self.memo[(m, n)] = res
        return res
    
sol = Solution()
print sol.uniquePaths(3, 2)