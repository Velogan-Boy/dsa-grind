# Last updated: 2/28/2026, 4:27:17 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]

        self.traverse(root,maxDiameter)

        return maxDiameter[0]

    def traverse(self, root: Optional[TreeNode], maxDiameter: list) -> int:

        if not root: return 0

        l = self.traverse(root.left,maxDiameter)
        r = self.traverse(root.right,maxDiameter)

        maxDiameter[0] = max(maxDiameter[0], l + r)

        return max(l,r) + 1




        