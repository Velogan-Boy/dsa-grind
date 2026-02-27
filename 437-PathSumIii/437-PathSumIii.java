// Last updated: 2/27/2026, 5:11:33 PM
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
    public int pathSum(TreeNode root, int targetSum) {

        HashMap<Long,Integer> map = new HashMap();

        map.put(0L,1);

        return pathSum2(root,0,targetSum,map);
        
    }

    public int pathSum2(TreeNode node, long runningSum , int target, HashMap<Long, Integer> map){

        if(node == null) return 0;

        runningSum += node.val;

        int count = map.getOrDefault(runningSum - target, 0);
        map.put(runningSum, map.getOrDefault(runningSum,0) + 1);

        count += pathSum2(node.left, runningSum, target, map);
        count += pathSum2(node.right, runningSum, target,map);

        map.put(runningSum, map.get(runningSum) - 1);

        return count;


    }
}