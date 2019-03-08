'''
Created on Mar 5, 2019

@author: omid
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack_keep_nodes = []
        stack_keep_values = []
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append(root)
                stack_keep_values.append(root.val) # root
                root = root.left # traverse left
            else:
                node = stack_keep_nodes.pop() # all left nodes traveresed so pop the last node
                root = node.right # traverse right
        return stack_keep_values
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack_keep_nodes = []
        stack_keep_values = []
        
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append(root)
                root = root.left
            else:
                node = stack_keep_nodes.pop()
                stack_keep_values.append(node.val)
                root = node.right
        return stack_keep_values
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack_keep_nodes = []
        stack_keep_values = []
        
        while root or stack_keep_nodes:
            if root:
                stack_keep_nodes.append(root)
                stack_keep_values.insert(0, root.val) # start from the root values and put them at the end
                root = root.right # traverse the right dont worry the values go to the start so right is after left
            else:
                node = stack_keep_nodes.pop()
                root = node.left # traverse left however the way that the values inserts in the value stack first left values get in front
        return stack_keep_values
    
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

   
# tree = TreeNode(1)
# right = TreeNode(2)
# right_left = TreeNode(3)
# tree.right = right
# right.left = right_left
tree = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
tree.left = left
tree.right = right
left_left = TreeNode(4)
left_right = TreeNode(5)
left.left = left_left
left.right = left_right

sol = Solution()
print sol.postorderTraversal(tree)