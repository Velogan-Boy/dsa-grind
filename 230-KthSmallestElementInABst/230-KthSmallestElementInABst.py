# Last updated: 2/28/2026, 4:27:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1
        ans = -1

        def inorderTraverse(node):
            nonlocal ans
            nonlocal i

            if not node: return

            inorderTraverse(node.left)
            if i == k: ans = node.val
            i+=1
            inorderTraverse(node.right)
        
        inorderTraverse(root)
        return ans
        
        


        