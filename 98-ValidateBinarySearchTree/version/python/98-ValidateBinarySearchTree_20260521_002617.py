# Last updated: 5/21/2026, 12:26:17 AM
1class Solution:
2    def isValidBST(self, root: Optional[TreeNode]) -> bool:
3        def isValid(node, low, high):
4            if not node:
5                return True
6            if not (low < node.val < high):
7                return False
8            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
9        return isValid(root, float('-inf'), float('inf'))