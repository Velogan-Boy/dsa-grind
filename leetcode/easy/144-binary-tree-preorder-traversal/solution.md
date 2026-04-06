# Binary Tree Preorder Traversal

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1970383473/
- **Date:** 2026-04-06

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans

        stack = [root]

        while stack:
            node = stack.pop()

            ans.append(node.val)

            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        

        return ans
        
```

---
*Generated automatically by LeetFeedback Extension*
