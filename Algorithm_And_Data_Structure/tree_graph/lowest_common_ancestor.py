class TreeNode():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
class Solution():
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # Now check if from both side we don't get any thing 
        if not left and not right:
            return None
        # This means that we get sth from both side and this node is the LCS
        if left and right:
            return root
        # So out of three cases; both null, both not null and one of them not null just the last one remains and we check it here
        return left if left else right
    
    
root = TreeNode(3)
right = TreeNode(1)
left = TreeNode(5)
root.right = right
root.left = left
left.left = TreeNode(6)
left.right = TreeNode(2)
left.right.left = TreeNode(7)
left.right.right = TreeNode(4)
right.left = TreeNode(0)
right.right = TreeNode(8)


sol = Solution()
p = right
q = left
print sol.lowestCommonAncestor(root, p, q).val

''' Java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        }
        if (root == p || root == q) {
            return root;
        }
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        // Now check what we get from both side
        if (left == null && right == null) {
            return null;
        }
        if (left != null && right != null) {
            return root;
        }
        // if left != null return left else return right
        return left != null ? left : right;
    }
}

'''

    