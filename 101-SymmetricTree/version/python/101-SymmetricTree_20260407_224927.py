# Last updated: 4/7/2026, 10:49:27 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    
9    def isSymmetric(self, root):
10
11        def isSameTree(p,q):
12            if not p and not q: return True
13            if not p or not q: return False
14
15            return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
16
17        return isSameTree(root.left, root.right)
18        
19        