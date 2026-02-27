// Last updated: 2/27/2026, 10:35:22 PM
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
        return lca(root,p,q);
    }

    public TreeNode lca(TreeNode node, TreeNode p , TreeNode q){

        if(node == null || node.val == p.val || node.val == q.val) return node;

        TreeNode l = lca(node.left,p,q);
        TreeNode r = lca(node.right,p,q);

        if(l == null && r == null) return null;

        if(l != null && r == null) return l;

        if(l == null && r != null) return r;

        else return node;
    }
}