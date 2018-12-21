import unittest
def is_valid_binary_tree_naive(tree_root):
    # DFS as we want to check if the binary tree is valid just if you wanted to check
    # the shortest path us BFS
    # The following does not work! It just check current node with its left and right
    # However it should check with the upper levels as well!!
    nodes = []
    nodes.append(tree_root)
    while len(nodes) > 0:
        node = tree_root.pop()
        value = node.value
        
        
        if node.left:
            nodes.append(node.left)
            if node.left.value > value:
                return False
        if node.right:
            nodes.append(node.right)
            if node.right.value < value:
                return False
            
    
    return True
    
def is_binary_search_tree(tree_root):
    # Stack to keep the traversal
    keep_nodes_limits = []
    keep_nodes_limits.append((tree_root, float('inf'), -float('inf')))
    
    while len(keep_nodes_limits) > 0:
        node, upper_bound, lower_bound = keep_nodes_limits.pop()
        
        # Now check that the value of the current node should be less than lower limit and bigger than higher limit
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False
        
        # Now push the left and right nodes to the stack
        # When the current node has left node the upper_bound should get changed and
        # the value of current node is the new upper_bound and vice-versa!!
        if node.left:
            keep_nodes_limits.append((node.left, node.value, lower_bound))
            
        if node.right:
            keep_nodes_limits.append((node.right, upper_bound, node.value))
            
    return True
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def is_binary_search_tree(root):
    # We need to define a stack for traversing the tree
    node_stack = [(root, -float('inf'), float('inf'))]
    
    #now loop over the tree and traverse the tree
    while len(node_stack):
        node, lower_bound, upper_bound = node_stack.pop()
        
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False
        # Since this is a stack it is LIFO so it first start from the right and goes deep as is DFS
        if node.left:
            node_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # Since the 
            node_stack.append((node.right, node.value, upper_bound))
            
    return True

class Test(unittest.TestCase):

    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            
        def insert_left(self, value):
            if self.value:
                if self.left is None:
                    self.left = Test.BinaryTreeNode(value)
                else:
                    self.left.insert_left(value)
            else:
                self.value = value
            return self.left            
        
        def insert_right(self, value):
            if self.value:
                if self.right is None:
                    self.right = Test.BinaryTreeNode(value)
                else:
                    self.right.insert_right(value)
            else:
                self.value = value
            return self.right
        
        def insert(self, value):
            #This function inset the value to generate the BST (Binary Search Tree)
            if self.value:
                # Check if the desired value is less than the node value
                if value < self.value:
                    if self.left is None:
                        self.left = Test.BinaryTreeNode(value)
                    else:
                        self.left.insert_left(value)
            elif value > self.value:
                if self.right is None:
                        self.right = Test.BinaryTreeNode(value)
                else:
                        self.right.insert_right(value)
            else:
                self.value = value
            return self.value
        def print_tree(self, tree):
            if self.left:
                self.left.print_tree(tree)
            print self.value
            if self.right:
                self.right.print_tree(tree)
                
            
                    
                    
        
    def test_is_binary_search_true(self):
        tree = self.BinaryTreeNode(50)
        tree.insert_left(30)
        tree.insert_right(80)
        tree.insert_left(20)
        tree.insert_left(5)
        tree.insert_right(10)
        tree.print_tree(tree)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)
        
        
unittest.main(verbosity=2)
    

    