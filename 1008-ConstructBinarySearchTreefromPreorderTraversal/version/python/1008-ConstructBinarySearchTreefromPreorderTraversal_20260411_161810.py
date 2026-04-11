# Last updated: 4/11/2026, 4:18:10 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def bstFromPreorder(self, A):
9        i = 0
10        
11        def helper(A, bound):
12            nonlocal i
13            if i == len(A) or A[i] > bound: return None
14
15            node = TreeNode(A[i])
16            i+=1
17            node.left = helper(A,node.val)
18            node.right = helper(A, bound)
19
20            return node
21            
22        return helper(A, inf)
23        