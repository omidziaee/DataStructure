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
print sol.dfs_inorder_rec_2(root)


        
                
                        
            