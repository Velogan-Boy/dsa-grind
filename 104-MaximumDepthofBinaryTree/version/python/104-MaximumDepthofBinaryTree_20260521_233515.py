# Last updated: 5/21/2026, 11:35:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9
10        def dfs(node):
11            if not node: return 0
12
13            left = dfs(node.left)
14            right = dfs(node.right)
15
16            return max(left, right) + 1
17
18        return dfs(root)
19        