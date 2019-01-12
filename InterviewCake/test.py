class Solution(object):
    def __init__(self):
        self.fib_memo = {}
    def fib(self, n):
    # Compute the nth Fibonacci number
    # Use memoization in order to save time
    # Base case
        if n < 0:
            raise ValueError("Input number should be greater than zero!")
        if n in [0, 1]:
            return n
        if n in self.fib_memo:
            return self.fib_memo[n]
        
        result = self.fib(n - 1) + self.fib(n - 2)
        self.fib_memo[n] = result
        return result
    
sol = Solution()
print sol.fib(5)














