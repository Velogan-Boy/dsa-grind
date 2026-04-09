# Last updated: 4/9/2026, 12:22:11 PM
1class Solution:
2    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
3        if not preorder or not inorder:
4            return None
5
6        root = TreeNode(preorder[0])
7        mid = inorder.index(preorder[0])
8
9        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
10        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
11
12        return root
13        
14        