# Last updated: 4/8/2026, 11:39:27 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3        if not root or root == p or root == q:
4            return root
5
6        left = self.lowestCommonAncestor(root.left, p, q)
7        right = self.lowestCommonAncestor(root.right, p, q)
8
9        if left and right:
10            return root
11
12        return left if left else right