'''
Created on Jan 1, 2020

@author: omid
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        # check the value of the root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
'''
#Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // This is eaier than BT however that we can solve it the same way
        // but here it is simpler as we know the nodes on the right side are all 
        // greater than the root and the nodes on the left side are all less than the root
        // for all the nodes recursively
        if (root == null) {return null;}
        if (root.val > Math.max(p.val, q.val)){
            // We know that the LCA is in the left side of the current node
            return lowestCommonAncestor(root.left, p, q);
        } else if (root.val < Math.min(p.val, q.val)) {
            // We need larger value which is going to be in the right side
            return lowestCommonAncestor(root.right, p, q);
        } else {
            // The root value is between the p and q values
            return root;
        }
    }
}
'''