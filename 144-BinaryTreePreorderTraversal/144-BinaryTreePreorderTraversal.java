// Last updated: 2/28/2026, 4:28:25 PM
/**
 * Definition for a binary tree TreeNode.
 * public class TreeTreeNode {
 *     int val;
 *     TreeTreeNode left;
 *     TreeTreeNode right;
 *     TreeTreeNode() {}
 *     TreeTreeNode(int val) { this.val = val; }
 *     TreeTreeNode(int val, TreeTreeNode left, TreeTreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> list = new ArrayList<>();

        if (root == null) {
            return list;
        }
 
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
 
        while (!stack.empty())
        {
            TreeNode curr = stack.pop();
 
            list.add(curr.val);

            if (curr.right != null) {
                stack.push(curr.right);
            }
 
            if (curr.left != null) {
                stack.push(curr.left);
            }
 


        }
        

        return list;
        
    }
}