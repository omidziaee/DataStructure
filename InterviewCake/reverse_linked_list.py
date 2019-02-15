'''
Created on Dec 6, 2018

@author: USOMZIA
'''


def reverse(head_of_list):

    # Reverse the linked list in place
    '''
    consider the following (it is better to consider it in multiple lines instead of
    one line, one line make it less comprehendable!!)
    a -> b
    b -> c
    c -> d
    d -> None (a->b->c->d->None)
    what we want is:
    a -> None
    b -> a
    c -> b
    d -> c (d->c->b->a->None)
    As it can be seen if the current_node.next points to the previous node it will be
    reversed!
    '''
    # The following reverses the linkedlist in one traverse
    current_node = head_of_list
    next_node = None
    previous_node = None
    
    # Traverse the list
    while current_node:
        # to swap the next node and previous node!
        # for the first iteration next_node = b
        # for the second iteration next_node = c
        # for the third iteration next_node = None
        next_node = current_node.next
        # for the first iteration a.next = None a->None
        # for the second iteration b.next = a b->a
        # for the third iteration c.next = b c->b
        current_node.next = previous_node
        
        # Now step forward
        # for the first iteration previous_node = a
        # for the second iteration previous_node = b
        # for the third iteration previous_node = c
        previous_node = current_node
        # for the first iteration current_node = b
        # for the second iteration current_node = c
        # for the third iteration current_node = None
        current_node = next_node
        # So now we have c->b->a->None
        
    return previous_node
        








class SinglyLinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None






a = SinglyLinkedList(1)
b = SinglyLinkedList(2)
c = SinglyLinkedList(3)
d = SinglyLinkedList(4)

a.next = b
b.next = c
c.next = d


print reverse(a)
            
        