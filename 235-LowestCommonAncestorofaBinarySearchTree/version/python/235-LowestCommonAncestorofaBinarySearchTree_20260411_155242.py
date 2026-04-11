# Last updated: 4/11/2026, 3:52:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if root is None:
11            return None
12
13        curr = root.val 
14
15        if curr < p.val and curr < q.val:
16            return self.lowestCommonAncestor(root.right, p, q)
17        
18        if curr > p.val and curr > q.val:
19            return self.lowestCommonAncestor(root.left, p, q)
20
21        return root
22