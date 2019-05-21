'''
Created on May 18, 2019

@author: omid
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1)
        temp = l3
        carry_over = 0
        while l1 and l2:
            x = l1.val + l2.val + carry_over
            temp.next = ListNode(x)
            if temp.next.val > 9:
                carry_over = temp.next.val / 10
                temp.next.val %= 10
            else:
                carry_over = 0
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        while l1:
            x = l1.val + carry_over
            temp.next = ListNode(x)
            if temp.next.val > 9:
                carry_over = temp.next.val / 10
                temp.next.val %= 10
            else:
                carry_over = 0
            temp = temp.next
            l1 = l1.next
        while l2:
            x = l2.val + carry_over
            temp.next = ListNode(x)
            if temp.next.val > 9:
                carry_over = temp.next.val / 10
                temp.next.val %= 10
            else:
                carry_over = 0
            l2 = l2.next
            temp = temp.next
        if carry_over > 0:
            temp.next = ListNode(carry_over)
            temp = temp.next
        return l3.next
    
# node1 = ListNode(2)
# next1 = ListNode(4)
# next11 = ListNode(3)
# node1.next = next1
# next1.next = next11
# node2 = ListNode(5)
# next2 = ListNode(6)
# next22 = ListNode(4)
# node2.next = next2
# next2.next = next22
node1 = ListNode(9)
next1 = ListNode(8)
node1.next = next1
node2 = ListNode(1)
sol = Solution()
print sol.addTwoNumbers(node1, node2)
