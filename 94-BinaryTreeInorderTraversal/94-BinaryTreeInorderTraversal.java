// Last updated: 7/12/2026, 6:23:36 PM
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
    public List<Integer> inorderTraversal(TreeNode root) {

        List<Integer> list = new ArrayList<>();

        Stack<TreeNode> stack = new Stack<TreeNode>();

        TreeNode currNode = root;

        while(!stack.isEmpty() || currNode != null){

            while(currNode != null ){
                stack.add(currNode);
                currNode = currNode.left;
            }

            currNode = stack.pop();
            list.add(currNode.val);
            currNode = currNode.right;
        }

        return list;


        
    }
}