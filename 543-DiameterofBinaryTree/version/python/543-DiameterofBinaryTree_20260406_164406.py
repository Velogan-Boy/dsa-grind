# Last updated: 4/6/2026, 4:44:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9
10        def helper(node, maxPath):
11            if not node: return 0
12
13            left = helper(node.left, maxPath)
14            right = helper(node.right, maxPath) 
15
16            maxPath[0] = max(maxPath[0], left + right)
17
18            return max(left, right) + 1
19
20        maxPath = [0]
21        helper(root, maxPath)
22
23        return maxPath[0]
24
25        
26        