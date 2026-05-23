# Last updated: 5/23/2026, 10:16:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def minCameraCover(self, root: Optional[TreeNode]) -> int:
10
11        # 0 -> not monitored
12        # 1 -> monitored, no camera
13        # 2 -> has camera
14
15        count = 0
16
17        def dfs(node):
18            nonlocal count
19
20            if not node:
21                return 1
22
23            l = dfs(node.left)
24            r = dfs(node.right)
25
26            if l == 0 or r == 0:
27                count += 1
28                return 2
29
30            if l == 2 or r == 2:
31                return 1
32
33            return 0
34
35        if dfs(root) == 0:
36            count += 1
37
38        return count