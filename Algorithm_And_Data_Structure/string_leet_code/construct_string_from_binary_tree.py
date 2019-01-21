'''
Created on Jan 19, 2019

@author: omid
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
'''
from __builtin__ import str
class Solution():
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # Do not forget about edge cases but do it at the end
        if not t:
            return ''
        tree_2_str = ''
        stack_to_keep_nodes = []
        stack_to_keep_nodes.append(t)
        
        while stack_to_keep_nodes:
            node = stack_to_keep_nodes.pop()
            if node == ")":
                tree_2_str += ")"
                continue
            tree_2_str += "(" + str(node.value)
            if not node.left and node.right:
                tree_2_str += '()'
            if node.right:
                stack_to_keep_nodes.append(")")
                stack_to_keep_nodes.append(node.right)
            if node.left:
                stack_to_keep_nodes.append(")")
                stack_to_keep_nodes.append(node.left)
        return tree_2_str[1:]
    # This one is preOrder traversal which to me is DFS recursive
    def tree2str_recursive(self, t):
        if t is None:
                return ""
            
        ans = str(t.value) 

        if t.left:
            ans+="(" + self.tree2str_recursive(t.left) + ")"

        if not t.left and t.right:
            ans+="()"

        if t.right:
            ans+="(" + self.tree2str_recursive(t.right) + ")"

        return ans
    
class BinaryTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

tree = BinaryTreeNode(1)
left = tree.insert_left(2)
right = tree.insert_right(3)
left.insert_left(4)
sol = Solution()
print sol.tree2str(tree)
            