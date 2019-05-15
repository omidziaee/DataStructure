<<<<<<< HEAD
'''
Created on Jan 13, 2019

@author: omid
'''
from test.badsyntax_future3 import result
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We need another input to show the index of the current stair
        memo = [0 for _ in range(n + 1)]
        index = 0
        return self.climb_stairs(index, n, memo)
    def climb_stairs(self, index, n, memo):
        # First check how is the recursive relation and if it is backward or forward
        # Normally backward is easier
        # Base case
        if index == n:
            return 1
        if index > n:
            return 0
        if memo[index] != 0:
            return memo[index]
        result = self.climb_stairs(index + 1, n, memo) + self.climb_stairs(index + 2, n, memo)
        memo[index] = result
        return result
    def climb_stairs_no_memo(self, index, n):
        if index == n:
            return 1
        if index > n:
            return 0
        result = self.climb_stairs_no_memo(index + 1, n) + self.climb_stairs_no_memo(index + 2, n)
        return result
    
    def climb_stairs_dp(self, n):
        if n <= 1:
            return n
        # From zero to n inclusive
        dp = [0 for i in range(n + 1)]
        dp [1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    def climb_stairs_dp_n_var(self, n):
        if n <= 1:
            return n
        prev = 1
        prev_prev = 2
        for i in range(3, n + 1):
            temp = prev
            prev = prev + prev_prev
            prev_prev = temp
        return prev

    def climbStairs_mem(self, n):
        import collections
        memo = collections.defaultdict()
        index = 0
        return self.climb_stairs_mem_dic(n, index, memo)
    def climb_stairs_mem_dic(self, n, index, memo):
        if index == n:
            return 1
        if index > n:
            return 0
        if index in memo:
            return memo[index]
        result = self.climb_stairs_mem_dic(n + 1, index, memo) + self.climb_stairs_mem_dic(n + 2, index, memo)
        memo[index] = result
        return result
            
            
        
            
       
            
import time            
sol = Solution()
start_time = time.time()
print sol.climb_stairs_dp_n_var(300)
=======
'''
Created on Jan 13, 2019

@author: omid
'''
from test.badsyntax_future3 import result
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We need another input to show the index of the current stair
        memo = [0 for _ in range(n + 1)]
        index = 0
        return self.climb_stairs(index, n, memo)
    def climb_stairs(self, index, n, memo):
        # First check how is the recursive relation and if it is backward or forward
        # Normally backward is easier
        # Base case
        if index == n:
            return 1
        if index > n:
            return 0
        if memo[index] != 0:
            return memo[index]
        result = self.climb_stairs(index + 1, n, memo) + self.climb_stairs(index + 2, n, memo)
        memo[index] = result
        return result
    def climb_stairs_no_memo(self, index, n):
        if index == n:
            return 1
        if index > n:
            return 0
        result = self.climb_stairs_no_memo(index + 1, n) + self.climb_stairs_no_memo(index + 2, n)
        return result
    
    def climb_stairs_dp(self, n):
        if n <= 1:
            return n
        # From zero to n inclusive
        dp = [0 for i in range(n + 1)]
        dp [1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    def climb_stairs_dp_n_var(self, n):
        if n <= 1:
            return n
        prev = 1
        prev_prev = 2
        for i in range(3, n + 1):
            temp = prev
            prev = prev + prev_prev
            prev_prev = temp
        return prev

    def climbStairs_mem(self, n):
        import collections
        memo = collections.defaultdict()
        index = 0
        return self.climb_stairs_mem_dic(n, index, memo)
    def climb_stairs_mem_dic(self, n, index, memo):
        if index == n:
            return 1
        if index > n:
            return 0
        if index in memo:
            return memo[index]
        result = self.climb_stairs_mem_dic(n + 1, index, memo) + self.climb_stairs_mem_dic(n + 2, index, memo)
        memo[index] = result
        return result
            
            
        
            
       
            
import time            
sol = Solution()
start_time = time.time()
print sol.climb_stairs_dp_n_var(300)
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print time.time() - start_time