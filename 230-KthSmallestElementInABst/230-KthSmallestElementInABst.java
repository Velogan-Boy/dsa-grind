// Last updated: 2/28/2026, 4:27:51 PM
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

    public int count = 0;

    public int kthSmallest(TreeNode root, int k) {

        if(root == null) return -1;

        int l = kthSmallest(root.left, k);

        count++;

        if(count == k) return root.val;

        int r = kthSmallest(root.right,k);

        return l < 0 ? r : l;
        
    }

  
}