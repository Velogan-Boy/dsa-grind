// Last updated: 2/27/2026, 10:35:42 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        
        boolean ans[] = new boolean[1];
        ans[0] = true;

        traverse(root, ans);

        return ans[0];

    }

    public int traverse(TreeNode root, boolean ans[]){

        if(root == null) return 0;

        int l = traverse(root.left, ans);
        int r = traverse(root.right, ans);

        if( Math.abs(l - r) > 1) ans[0] = false;

        return Math.max(l,r) + 1;

    }
}