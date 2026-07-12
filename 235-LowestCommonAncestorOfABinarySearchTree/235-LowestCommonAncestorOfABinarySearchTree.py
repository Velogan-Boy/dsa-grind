# Last updated: 7/12/2026, 6:20:48 PM
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root