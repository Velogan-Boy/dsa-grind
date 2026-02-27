// Last updated: 2/27/2026, 5:03:04 PM

 class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null)return root;
        // search the node which we want to delete 
        if(root.val < key) root.right = deleteNode(root.right , key);
        else if (root.val > key) root.left = deleteNode(root.left ,key);        
        else{
            // case 1: when node to be deleted is leaf node
            if(root.left == null && root.right == null)return null;
            // case 2 : node to be deleted is having only right sub tree
            else if(root.left == null) return root.right;
            // case 2: node to be deleted is having only left sub tree
            else if(root.right == null) return root.left;
            // case 3 : node having both childrens then get max from left subtree and solve
            // copy the min val from right subtree to the node
            root.val =  getMaxValNode(root.left);
            // this case is now reduced to the case 1 or case 2
            root.left=deleteNode(root.left,root.val);
        }
        return root;
    }
    // function for geting the max form left subtree
    public int getMaxValNode(TreeNode root ){
       int max=root.val;
        while(root !=null){
            max = root.val;
            root=root.right;
        }
        return max;
    }
}