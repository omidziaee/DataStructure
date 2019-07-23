'''
Created on Jul 11, 2019

@author: USOMZIA
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution():
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        i = 0
        while head:
            if head in dic:
                return dic[head]
            else:
                dic[head] = i
                i += 1
                head = head.next
        return None
    def detect_cycle_two_pointer(self, head):
        # Here we use the fact that fast pointer traverse twice than slower pointer
        # It means that the distance that the fast pointer traverse is twice the distance
        # that the slow pointer traverse
        intersect_node = self.intersect_point(head)
        if intersect_node is None:
            return None
        # Now we need to find the start of the loop
        head_keep = head
        while head_keep != intersect_node:
            head_keep = head_keep.next
            intersect_node = intersect_node.next
        return intersect_node
    def intersect_point(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            if fast.next.next == slow.next:
                return slow.next
            fast = fast.next.next
            slow = slow.next
        return None
    
    
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

sol = Solution()
print sol.detectCycle(head)

