'''
Created on Oct 24, 2019

@author: USOMZIA
Given a (singly) linked list with head node root, write a function to split the linked list 
into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size 
differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier 
should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, 
and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = 1
        dummy_head = root
        while dummy_head:
            dummy_head = dummy_head.next
            n += 1
        w, r = divmod(n, k)
        current = root
        res = []
        for i in range(k):
            dum = trav = ListNode(None)
            for j in range(w + (i < r)):
                trav.next = trav = ListNode(current.val)
                if current: current = current.next
            res.append(dum.next)
        return res
                
    
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)
node_7 = ListNode(7)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_7

sol = Solution()
print sol.splitListToParts(node_1, 3)