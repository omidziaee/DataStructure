'''
Created on Apr 5, 2019

@author: USOMZIA
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # count the number of nodes
        temp_head = head
        counter = 0
        while temp_head:
            temp_head = temp_head.next
            counter += 1
        i = 0
        dummy_node = ListNode(0)
        dummy_node.next = head
        temp_head = dummy_node
        while i < counter - n and temp_head:
            temp_head = temp_head.next
            i += 1
        temp_head.next = temp_head.next.next
        return dummy_node.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3 
node3.next = node4
node4.next = node5           
sol = Solution()
print sol.removeNthFromEnd(node1, 2)