'''
Created on Oct 18, 2019

@author: USOMZIA
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        # Do not change head always create dummy nodes!
        # Now find the tail and attach it to the head. The same time find the number of nodes.
        old_tail = head
        list_length = 1
        while old_tail.next:
            old_tail = old_tail.next
            list_length += 1
        old_tail.next = head # Attach the last node to head
        # Now traverse again to detach the n - k%n - 1 
        new_tail = head # Again start from head
        for i in range(list_length - k%list_length - 1):
            new_tail = new_tail.next
        new_head = new_tail.next # Do not forget to create new head
        new_tail.next = None
        return new_head