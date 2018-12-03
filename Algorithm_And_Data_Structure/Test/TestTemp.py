'''
Created on Nov 28, 2018

@author: USOMZIA
'''
def find_biggest_node(tree):
    # base case
    if not tree.right:
        return tree.value
    return find_biggest_node(tree.right)



class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    

tree = BinaryTreeNode(50)
left = tree.insert_left(40)
right = tree.insert_right(60)
left.insert_left(30)
left.insert_right(45)
print find_biggest_node(tree)
        
    