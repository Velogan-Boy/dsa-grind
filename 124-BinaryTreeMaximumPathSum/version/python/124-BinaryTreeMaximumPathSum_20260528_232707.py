# Last updated: 5/28/2026, 11:27:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10
11        globalMax = float('-inf')
12
13        def dfs(node):
14            nonlocal globalMax
15
16            if not node:
17                return 0
18
19            l = max(0, dfs(node.left))
20            r = max(0, dfs(node.right))
21
22            globalMax = max(globalMax, l + r + node.val)
23
24            return node.val + max(l, r)
25
26        dfs(root)
27
28        return globalMax