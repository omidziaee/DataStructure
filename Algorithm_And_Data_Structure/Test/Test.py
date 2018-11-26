import unittest




class Test(unittest.TestCase):
    #Define the node definition class
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.root = value
            self.left = None
            self.right = None
        
        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left
    
        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right
    

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(1)

        left.insert_left(4)
        left.insert_right(3)

        right.insert_left(7)
        right.insert_right(6)
   


