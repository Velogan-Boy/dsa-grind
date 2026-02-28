# Last updated: 2/28/2026, 4:28:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            output.append(node.val)
   
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

      
        return output[::-1]
        
        