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
    #-------this is no good------------
    def sortList_not_good(self, head):
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
    #---------------------------------
    def sort_list(self, head):
        if not head or not head.next:
            return head
        middle = self.find_middle_node(head)
        # create the right half head node
        right = middle.next
        # separate the right half and left half
        middle.next = None
        # send the head of left half and head of right half to the merge function
        left_side = self.sort_list(head)
        right_side = self.sort_list(right)
        return self.merge(left_side, right_side)
    def find_middle_node(self, head):
        slow, fast = head, head
        # fast.next and fast.next.next both needs to get checked
        # fast.next for the case it reaches the end like l5 here because
        # next.next is nothing meaning nonetype it raise an error
        # fase.next.next is for fast = fast.next.next because otherwise it 
        # is going to be none and it causes an issue
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def merge(self, head1, head2):
        # This is a dummy node to set for merged lists val is not important
        dummy = ListNode(-1)
        # this is a pointer to traverse the dummy because we need the head of dummy for return
        pointer_node = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                pointer_node.next = head1
                head1 = head1.next
            else:
                pointer_node.next = head2
                head2 = head2.next
            pointer_node = pointer_node.next
        pointer_node.next = head1 if head1 else head2
        return dummy.next
        
    
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(1)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

sol = Solution()
print sol.find_middle_node(l1)


