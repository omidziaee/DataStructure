'''
Created on May 31, 2019

@author: USOMZIA
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
 before the intersected node in A; There are 3 nodes before the intersected node in B.
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode_2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        d_set_A = set()
        p_a = headA
        while p_a:
            d_set_A.add(p_a)
            p_a = p_a.next
        p_b = headB
        find_intersection = False
        while p_b and not find_intersection:
            if p_b in d_set_A:
                find_intersection = True
            p_b = p_b.next
        return p_b
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        # Always define pointers otherwise you will loose the location of head
        p_a = headA
        p_b = headB
        len_a = 0
        len_b = 0
        while p_a:
            len_a += 1
            p_a = p_a.next
        while p_b:
            len_b += 1
            p_b = p_b.next
        # Now find which one is longer and move the longer one to reach the same location on the
        # shorter one!
        p_a = headA
        p_b = headB
        if len_a > len_b:
            diff = len_a - len_b
            while diff > 0:
                p_a = p_a.next
                diff -= 1
        else:
            diff = len_b - len_a
            while diff > 0:
                p_b = p_b.next
                diff -= 1
        # Now both starts at the same location if they have itersection
        # we need to check if from the current node up to the end all the nodes are the same.
        # If from the intersection up to the end all the nodes are the same we can say that is
        # a real intersection!
        
        while p_a != p_b:
            print p_a.val, p_b.val
            p_a = p_a.next
            p_b = p_b.next
        return p_a
            
        
            
A = ListNode(8)
A1 = ListNode(4)
A2 = ListNode(5)
B = ListNode(4)
B1 = ListNode(1)
B2 = ListNode(8)
B3 = ListNode(4)
B4 = ListNode(5)
A.next = A1
A1.next = A2
B.next = B1
B1.next = B2
B2.next = B3
B3.next = B4
sol = Solution()
print sol.getIntersectionNode(A, B)