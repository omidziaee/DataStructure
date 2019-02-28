'''
Created on Feb 16, 2019

@author: omid
'''
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        
class Solution():
    def merged_two_sorted_list(self, l1, l2):
        # This is the recursive solution
        # First we check if any of the two list is null then return the other one 
        # this is the base case
        if not l1:
            return l2
        if not l2:
            return l1
        # Now it is time to check the head of each one is less than the head of the 
        # other one!!
        if (l1.val <= l2.val):
            l1.next = self.merged_two_sorted_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merged_two_sorted_list(l1, l2.next)
            return l2
        
    def merged_two_lists_loop(self, l1, l2):
        #Todo: Edge cases
        # The idea is to create another linked list ans initialize it to sth
        # also define a pointer to traverse the two lists based on the values
        # The initial value is totally arbitrary you can say anything
        l3 = ListNode(-1)
        # This is the pointer
        prev = l3
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            # need to move the prev to the next one
            prev = prev.next
        # You always should move the pointer not l3 cause l3 is prev right!!
        prev = l1 if l1 else l2
        return l3.next
        
    
    
    


    
l1 = ListNode(1)
l11 = ListNode(4)
l12 = ListNode(5)
l1.next = l11
l11.next = l12
l2 = ListNode(1)
l21 = ListNode(2)
l22 = ListNode(3)
l23 = ListNode(6)
l2.next = l21
l21.next = l22
l22.next = l23
