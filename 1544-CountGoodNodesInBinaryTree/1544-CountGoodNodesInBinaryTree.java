// Last updated: 2/27/2026, 5:11:09 PM
class Solution {

    public int goodNodes(TreeNode root) {
        return traverse(root, Integer.MIN_VALUE );
    }

    private int traverse(TreeNode root, int max) {
        if (root == null) return 0;

        if (root.val >= max) {
            max = root.val;
            return 1 + traverse(root.left, max) + traverse(root.right, max);
        }

        return traverse(root.left, max) + traverse(root.right, max);
    }
}