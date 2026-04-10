# Last updated: 4/10/2026, 5:37:02 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        node = root
11
12        while node:
13            if node.val == val:
14                return node
15            elif val < node.val:
16                node = node.left
17            else:
18                node = node.right
19        
20        return None
21        
22        