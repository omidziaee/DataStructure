'''
Created on Feb 28, 2019

@author: USOMZIA
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.min = float('inf')
        min_stack_get = MinStack
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        self.min = min(self.min, x)
        min_stack_get.q.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        temp = self.q.pop()
        if temp == min_stack_get.q[-1]:
            min_stack_get.q.pop()
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        
        if len(self.q) == 0:
            return None
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()