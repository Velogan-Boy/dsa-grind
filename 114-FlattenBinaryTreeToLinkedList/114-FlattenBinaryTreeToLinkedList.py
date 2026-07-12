# Last updated: 7/12/2026, 6:22:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def buildTree(curr: TreeNode):
            nonlocal p 
            if not curr: return

            if p:
                p.right = curr
                p.left = None
            
            p = curr
            r = curr.right

            buildTree(curr.left)
            buildTree(r)


        
        p = None
        buildTree(root)




        