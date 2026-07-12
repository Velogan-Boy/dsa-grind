# Last updated: 7/12/2026, 6:17:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, A):
        i = 0
        
        def helper(A, bound):
            nonlocal i
            if i == len(A) or A[i] > bound: return None

            node = TreeNode(A[i])
            i+=1
            node.left = helper(A,node.val)
            node.right = helper(A, bound)

            return node
            
        return helper(A, inf)
        