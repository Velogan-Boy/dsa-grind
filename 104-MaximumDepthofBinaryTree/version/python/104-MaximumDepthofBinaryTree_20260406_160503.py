# Last updated: 4/6/2026, 4:05:03 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9
10        def helper(node):
11            if not node: return 0
12
13            return max(helper(node.left), helper(node.right)) + 1
14
15        return helper(root)
16        