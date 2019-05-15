'''
Created on Feb 28, 2019

@author: USOMZIA
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys
 greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Preorder and add them up
Initial Thoughts
This question asks us to modify an asymptotically linear number of nodes in a given binary search tree, so a very efficient solution will visit each node once. 
The key to such a solution would be a way to visit nodes in descending order, keeping a sum of all values that we have already visited and adding that sum to the
node's values as we traverse the tree. This method for tree traversal is known as a reverse in-order traversal, and allows us to guarantee visitation of each node 
in the desired order. The basic idea of such a traversal is that before visiting any node in the tree, we must first visit all nodes with greater value. Where are
all of these nodes conveniently located? In the right subtree.

Approach #1 Recursion [Accepted]
Intuition

One way to perform a reverse in-order traversal is via recursion. By using the call stack to return to previous nodes, we can easily visit the nodes in reverse
order.
Algorithm
For the recursive approach, we maintain some minor "global" state so each recursive call can access and modify the current total sum. Essentially, we ensure 
that the current node exists, recurse on the right subtree, visit the current node by updating its value and the total sum, and finally recurse on the left subtree.
If we know that recursing on root.right properly updates the right subtree and that recursing on root.left properly updates the left subtree, then we are
guaranteed to update all nodes with larger values before the current node and all nodes with smaller values after.
'''
# this is reverse in order traversal to visit all the higher value nodes first then traverse to the lower values
# But you need global memory that is being shared with all of the recursions
class Solution(object):
    class Solution(object):
        def  __init__(self):
            self.total = 0
        def convertBST(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            return self.dfs(root)
        
        def dfs(self, root):
            if root:
                self.dfs(root.right)
                self.total += root.val
                root.val = self.total
                self.dfs(root.left)
            return root
    
    
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        