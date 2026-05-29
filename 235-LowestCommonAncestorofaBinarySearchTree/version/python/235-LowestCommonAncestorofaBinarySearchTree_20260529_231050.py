# Last updated: 5/29/2026, 11:10:50 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3
4        def dfs(node):
5            if not node:
6                return None
7
8            if node == p or node == q:
9                return node
10
11            left = dfs(node.left)
12            right = dfs(node.right)
13
14            if left and right:
15                return node
16
17            return left if left else right
18
19        return dfs(root)