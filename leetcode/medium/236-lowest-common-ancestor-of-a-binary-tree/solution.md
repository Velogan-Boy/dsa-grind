# Lowest Common Ancestor of a Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1972883654/
- **Date:** 2026-04-08

## Solution

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
```

---
*Generated automatically by LeetFeedback Extension*
