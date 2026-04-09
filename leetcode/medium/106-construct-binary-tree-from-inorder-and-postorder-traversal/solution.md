# Construct Binary Tree from Inorder and Postorder Traversal

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1973292464/
- **Date:** 2026-04-09

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid],postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])

        return root
        
        
```

---
*Generated automatically by LeetFeedback Extension*
