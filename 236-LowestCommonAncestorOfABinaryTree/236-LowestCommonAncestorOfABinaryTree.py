# Last updated: 7/12/2026, 6:20:47 PM
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = None

        def traverse(node):
            nonlocal ans
            if not node:
                return False

            left = traverse(node.left)
            right = traverse(node.right)

            mid = (node == p or node == q)

            if mid + left + right >= 2:
                ans = node

            return mid or left or right

        traverse(root)
        return ans