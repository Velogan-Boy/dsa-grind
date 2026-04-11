# Last updated: 4/11/2026, 3:37:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
9        self.ans = float('inf')
10        min1 = root.val
11
12        def dfs(node):
13            if node:
14                if min1 < node.val < self.ans:
15                    self.ans = node.val
16                elif node.val == min1:
17                    dfs(node.left)
18                    dfs(node.right)
19
20        dfs(root)
21        return self.ans if self.ans < float('inf') else -1
22        