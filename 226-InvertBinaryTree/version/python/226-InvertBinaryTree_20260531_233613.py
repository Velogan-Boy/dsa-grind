# Last updated: 5/31/2026, 11:36:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9
10        def dfs(node):
11            if not node: return
12
13            l = dfs(node.left)
14            r = dfs(node.right)
15
16            temp = node.left
17            node.left = node.right
18            node.right = temp
19
20        dfs(root)
21
22        return root
23
24
25
26
27        