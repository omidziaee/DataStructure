'''
Created on Dec 10, 2018

@author: USOMZIA
'''
class Fibber(object):
    def __init__(self):
        # The follwoing Dic is to store the instaces that we already calculate
        self.memo = {}
        
    def fib(self, n):
        if n < 0:
            raise IndexError("index is negative and it can not be happen!")
        # As it is recursive it needs a Base case
        if n in [0, 1]:
            return n
        
        # Now it is time to check if we have already calculte this or not
        if n in self.memo:
            print "This comes from memo[%i]" % n
            return self.memo[n]
        print "This is a new calculation! %i" %n
        result = self.fib(n - 1) + self.fib(n - 2)
        
        # Memoize the current Calculation
        self.memo[n] = result
        
        return result
    
    def fib_no_memo(self, n):
        if n < 0:
            raise IndexError("n can not be less than zero!")
        # Base case
        if n in [0, 1]:
            return n
        # Because first function is n - 1 it went down and calculate all the way to 0 and one from the left side and then
        # comes up to calculate the n - 2
        return self.fib_no_memo(n - 1) + self.fib_no_memo(n - 2)
    
sol = Fibber()
print sol.fib_no_memo(6)