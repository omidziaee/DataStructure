'''
Created on May 10, 2019

@author: omid
'''
class Solution():
    def __init__(self):
        self.memo = {}
    def find_fib(self, n):
        if n < 3:
            return n
        if n in self.memo:
            return self.memo[n]
        res = self.find_fib(n - 1) + self.find_fib(n - 2)
        self.memo[n] = res
        return res
    def find_fib_dp(self, n):
        if n < 3:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
    def find_fib_dp2(self, n):
        if n < 3:
            return n
        prev = 2
        prev_prev = 1
        for _ in range(3, n + 1):
            temp = prev
            curr = prev + prev_prev
            prev = curr
            prev_prev = temp
        return curr
            
            
    
import time
start_time = time.time()
sol = Solution()
print sol.find_fib_dp2(100)
print time.time() - start_time                
