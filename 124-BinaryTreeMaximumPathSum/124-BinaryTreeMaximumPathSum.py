# Last updated: 7/12/2026, 6:22:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        globalMax = float('-inf')

        def dfs(node):
            nonlocal globalMax

            if not node:
                return 0

            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            globalMax = max(globalMax, l + r + node.val)

            return node.val + max(l, r)

        dfs(root)

        return globalMax