// Last updated: 2/27/2026, 9:36:56 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    int index = 0;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {

        if(root == null) return "#,";

        return root.val + "," + serialize(root.left) + serialize(root.right);

        
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {


        if(index >= data.length()) return null;

        if(data.charAt(index) == '#') {

            index += 2;

            
            return null;

        }
            

        int start = index;
        int end = index;

        while(data.charAt(end) != ','){
            end++;
        }
        TreeNode node = new TreeNode(Integer.parseInt(data.substring(start,end)) );

        index = end + 1;

        node.left = deserialize(data);
        node.right = deserialize(data);

        return node;



        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));