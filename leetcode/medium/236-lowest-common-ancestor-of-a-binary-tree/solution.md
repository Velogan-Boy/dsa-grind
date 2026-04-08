# Lowest Common Ancestor of a Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1972890722/
- **Date:** 2026-04-08

## Solution

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = None

        def traverse(node):
            nonlocal ans
            if not node:
                return False

            left = traverse(node.left)
            right = traverse(node.right)

            mid = (node == p or node == q)

            if mid + left + right >= 2:
                ans = node

            return mid or left or right

        traverse(root)
        return ans
```

---
*Generated automatically by LeetFeedback Extension*
