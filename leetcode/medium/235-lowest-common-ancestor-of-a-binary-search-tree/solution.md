# Lowest Common Ancestor of a Binary Search Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- **Date:** 2026-05-29

## Solution

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def dfs(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right

        return dfs(root)
```

---
*Generated automatically by LeetFeedback Extension*
