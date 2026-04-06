# Last updated: 4/6/2026, 5:11:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9
10        def helper(node, maxPathSum):
11            if not node: return 0
12
13            left = max(0, helper(node.left, maxPathSum))
14            right = max(0, helper(node.right, maxPathSum))
15
16            maxPathSum[0] = max(maxPathSum[0], left + right + node.val)
17
18            return max(left,right) + node.val
19
20        maxPathSum = [-inf]
21        helper(root,maxPathSum)
22
23        return maxPathSum[0]
24        
25        