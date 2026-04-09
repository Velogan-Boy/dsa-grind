# Last updated: 4/9/2026, 12:14:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        if not inorder or not postorder:
10            return None
11
12        root = TreeNode(postorder[-1])
13        mid = inorder.index(postorder[-1])
14
15        root.left = self.buildTree(inorder[:mid],postorder[:mid])
16        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
17
18        return root
19        
20        