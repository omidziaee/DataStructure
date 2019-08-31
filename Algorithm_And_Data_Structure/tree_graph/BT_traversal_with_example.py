class Solution():
    def dfs_preorder(self, root):
        stack = []
        keep_values = []
        while root or stack:
            if root:
                stack.append(root)
                keep_values.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return keep_values
    
    def dfs_inorder(self, root):
        stack = []
        keep_values = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                keep_values.append(node.val)
                root = node.right
        return keep_values
    
    def dfs_inorder_rec(self, root):
        if not root:
            return []
        
        return self.helper_inorder(root)
    def helper_inorder(self, root):
        if not root:
            return []
        return self.helper_inorder(root.left) + [root.val] + self.helper_inorder(root.right)
    
    def dfs_inorder_rec_2(self, root):
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if not root:
            return []
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
        return res
    
    def dfs_postorder_rec(self, root):
        if not root:
            return []
        return self.helper_postorder(root)
    def helper_postorder(self, root):
        if not root:
            return []
        return self.helper_postorder(root.left) + self.helper_postorder(root.right) + [root.val]
    def dfs_postorder(self, root):
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
                
        
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
        
        
    
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left_left = TreeNode(4)
left_left_left = TreeNode(5)
left_left_right = TreeNode(6)
left_left_left_right = TreeNode(7)
right_left = TreeNode(8)
right_left_right = TreeNode(9)
right_right = TreeNode(10)
root.left = left
root.right = right
left.left = left_left
left.left.left = left_left_left
left.left.right = left_left_right
left.left.left.right = left_left_left_right
right.left = right_left
right.left.right = right_left_right
right.right = right_right

sol = Solution()
print sol.dfs_postorder(root)


        
                
                        
            