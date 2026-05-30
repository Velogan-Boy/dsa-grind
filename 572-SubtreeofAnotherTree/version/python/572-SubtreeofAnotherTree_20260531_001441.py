# Last updated: 5/31/2026, 12:14:41 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9
10        if not subRoot: return True
11
12
13        def dfs(node):
14            if not node: return False
15
16            if node.val == subRoot.val and self.isSameTree(node, subRoot):
17                return True
18
19            return dfs(node.left) or dfs(node.right)
20
21        return dfs(root)
22
23    def isSameTree(self, p, q):
24        if not p and not q: return True
25
26        if not p or not q: return False
27
28        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
29        