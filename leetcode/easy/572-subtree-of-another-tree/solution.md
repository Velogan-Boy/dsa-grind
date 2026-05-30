# Subtree of Another Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/subtree-of-another-tree/submissions/2017512522/
- **Date:** 2026-05-30

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True


        def dfs(node):
            if not node: return False

            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)

    def isSameTree(self, p, q):
        if not p and not q: return True

        if not p or not q: return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
```

---
*Generated automatically by LeetFeedback Extension*
