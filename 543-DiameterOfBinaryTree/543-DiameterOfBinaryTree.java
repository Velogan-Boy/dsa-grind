// Last updated: 2/28/2026, 4:27:19 PM
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
    public int diameterOfBinaryTree(TreeNode root) {
        
        int max[] = new int[1];

        traverse(root, max);

        return max[0];

    }


    public int traverse(TreeNode root, int max[]){

        if(root == null) return 0;

        int l = traverse(root.left, max);
        int r = traverse(root.right,max);

        max[0] = Math.max(l + r, max[0]);

        return Math.max(l , r) + 1;

    }
}