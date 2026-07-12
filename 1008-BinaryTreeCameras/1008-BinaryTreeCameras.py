# Last updated: 7/12/2026, 6:17:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        # 0 -> not monitored
        # 1 -> monitored, no camera
        # 2 -> has camera

        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return 1

            l = dfs(node.left)
            r = dfs(node.right)

            if l == 0 or r == 0:
                count += 1
                return 2

            if l == 2 or r == 2:
                return 1

            return 0

        if dfs(root) == 0:
            count += 1

        return count