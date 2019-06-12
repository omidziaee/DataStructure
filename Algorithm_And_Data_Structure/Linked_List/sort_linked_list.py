'''
Created on May 14, 2019

@author: omid
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
class Solution():
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return sorted(res)
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(1)
l1.next = l2
l2.next = l3
l3.next = l4

sol = Solution()
print sol.sortList(l1)


