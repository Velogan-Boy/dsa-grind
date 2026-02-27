// Last updated: 2/27/2026, 5:22:23 PM
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
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0) return null;
        if(nums.length == 1) return new TreeNode(nums[0]);
        return convert(nums,0,nums.length - 1);
    }

    public TreeNode convert(int[] nums,int start, int end){
        if(start > end) return null;
        
        int mid = start + (end - start) / 2;

        TreeNode node = new TreeNode(nums[mid]);

        node.left = convert(nums,start,mid - 1);
        node.right = convert(nums,mid + 1, end);

        return node;

    }
}