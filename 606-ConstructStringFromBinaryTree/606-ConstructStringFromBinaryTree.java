// Last updated: 2/27/2026, 10:35:06 PM
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
    public String tree2str(TreeNode root) {
        
        if(root == null) return "";
        
        String str = "";

        str += root.val;

        if(root.left == null && root.right == null) return str;

        if(root.left == null && root.right != null){
            str += "()";
            str += '(';
            str += tree2str(root.right);
            str += ')';
        }else if(root.left != null && root.right == null){
            str += '(';
            str += tree2str(root.left);
            str += ')';
        }else{
            str += '(';
            str += tree2str(root.left);
            str += ')';

            str += '(';
            str += tree2str(root.right);
            str += ')';


        }

            

          

        return str;



        
    }
}