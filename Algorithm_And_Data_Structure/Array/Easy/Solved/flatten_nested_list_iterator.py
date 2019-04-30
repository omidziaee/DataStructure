'''
Created on Apr 27, 2019

@author: omid
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = str(nestedList)
        self.counter = 0
    def next(self):
        """
        :rtype: int
        """
        return self.nestedList[self.counter]

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.counter < len(self.nestedList) and self.nestedList[self.counter] != "[":
            self.counter += 1
        if self.counter < len(self.nestedList) and self.nestedList[self.counter] == "[":
            while self.counter < len(self.nestedList) and self.nestedList[self.counter] == "[":
                self.counter += 1
            return True
        else:
            return False
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
sol = NestedIterator([1,[4,[6]]])
