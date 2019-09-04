'''
Created on Sep 1, 2019

@author: omid
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
'''
# The following is brute-force as each time new appointment comes it searches from start
class MyCalender1():
    def __init__(self):
        self.calender = []
    def book(self, start, end):
        for s, e in self.calender:
            if start < e and s < end:
                return False
        self.calender.append((start, end))
        return True
    
    
    
class MyCalendar(object):
    def __init__(self):
        self.calender = None
    def book(self, start, end):
        # If it is empty this is the initialization and we don't need to
        # call insert
        if not self.calender:
            self.calender = TreeNode(start, end)
            return True
        else:
            return self.calender.insert(TreeNode(start, end))

class TreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.right = None
        self.left = None
    def insert(self, node):
        # This function insert to the BST
        # if start of the new node is greater than the
        # start of the current node then it shoud go to the right
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        else:
            return False
    
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
sol = MyCalendar()   
print sol.book(10, 20)
print sol.book(15, 25)
print sol.book(20, 30)
    
            
        