'''
Created on Aug 31, 2019

@author: omid
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution():
    def sortedListToBST(self, head):
        if not head:
            raise Exception("List should not be empty")
        arr_list = self.list_to_array(head)
        return self.array_to_tree_faster(arr_list, 0, len(arr_list) - 1)
        #return self.array_to_tree(arr_list)
    
    def list_to_array(self, head):
        dum_head = head
        arr_list = []
        while dum_head:
            arr_list.append(dum_head.val)
            dum_head = dum_head.next
        return arr_list
            
    def array_to_tree(self, arr_list):
        if not arr_list:
            return None
        # This can have -1 or not mid = len(arr_list)) / 2 is also true
        mid = (len(arr_list) - 1) / 2
        b = arr_list[mid]
        root = TreeNode(b)
        root.left = self.array_to_tree(arr_list[:mid])
        root.right = self.array_to_tree(arr_list[mid + 1:])
        return root
        
    def array_to_tree_faster(self, arr_list, l, r):
        # less than because for equal we also need to return sth
        if l > r:
            return None
        mid = l + (r - l) / 2
        root = TreeNode(arr_list[mid])
        # left and right are not always 0 and mid - 1 as we send the arr_list
        # we actually update the left and right 
        # So when we traverse left we update right and when we traverse left 
        # we update left
        root.left = self.array_to_tree_faster(arr_list, l, mid - 1)
        root.right = self.array_to_tree_faster(arr_list, mid + 1, r)
        return root
    #===========================================================================
    def sorted_list_to_tree(self, head):
        if not head:
            return None
        # Find the mid point
        mid = self.find_mid(head)
        # create a TreeNode of mid
        root = TreeNode(mid.val)
        if head == mid:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    
    def find_mid(self, head):
        # Prev is to disjoint left and right part
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # disjoint the left and right part   
        if prev:
            prev.next = None
        return slow
    
    
        
        
            
node0 = ListNode(-10)
node1 = ListNode(-3)
node2 = ListNode(0)
node3 = ListNode(5)
node4 = ListNode(9)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
sol = Solution()
head = node0
print sol.sortedListToBST(head).val

    