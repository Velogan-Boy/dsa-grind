# Last updated: 5/29/2026, 11:12:55 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3
4        if p.val < root.val and q.val < root.val:
5            return self.lowestCommonAncestor(root.left, p, q)
6
7        if p.val > root.val and q.val > root.val:
8            return self.lowestCommonAncestor(root.right, p, q)
9
10        return root