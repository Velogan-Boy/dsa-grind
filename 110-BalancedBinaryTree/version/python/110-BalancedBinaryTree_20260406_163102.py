# Last updated: 4/6/2026, 4:31:02 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9
10        def helper(node, isBalanced):
11            if not node: return 0
12
13            left = helper(node.left, isBalanced) + 1
14            right = helper(node.right, isBalanced) + 1
15
16            if abs(left - right) > 1: isBalanced[0] = False
17
18            return max(left, right)
19
20        isBalanced = [True]
21
22        helper(root, isBalanced)
23
24        return isBalanced[0]
25
26
27        