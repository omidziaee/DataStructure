'''
Created on Apr 5, 2019

@author: USOMZIA
'''
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) == self.size:
            self.window.pop(0)
        self.window.append(val)
        return float(sum(self.window)) / min(self.size, len(self.window))
    
sol = MovingAverage(3)
print sol.next(1)
print sol.next(10)
