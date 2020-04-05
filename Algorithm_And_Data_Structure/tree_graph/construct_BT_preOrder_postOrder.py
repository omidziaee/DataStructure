'''
Created on Mar 24, 2020

@author: omidziaee
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
'''
class Solution():
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1: L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:])
        return root
    def traverse(self, root):
        if not root:
            return None
        nodes = []
        self.pre_order(root, nodes)
        return nodes
    def post_order(self, root, nodes):
        if not root:
            return None
        self.post_order(root.left, nodes)
        self.post_order(root.right, nodes)
        nodes.append(root.val)
        
    def pre_order(self, root, nodes):
        if not root:
            return None
        nodes.append(root.val)
        self.pre_order(root.left, nodes)
        self.pre_order(root.right, nodes)
    
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left_left = TreeNode(4)
Left_right = TreeNode(5)
right_left = TreeNode(6)
right_right = TreeNode(7)
root.left = left
root.right = right
left.left = left_left
left.right = Left_right 
right.left = right_left
right.right = right_right

sol = Solution()
print sol.traverse(root)