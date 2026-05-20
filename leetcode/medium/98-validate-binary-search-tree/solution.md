# Validate Binary Search Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/validate-binary-search-tree/submissions/2008457431/
- **Date:** 2026-05-20

## Solution

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
        return isValid(root, float('-inf'), float('inf'))
```

---
*Generated automatically by LeetFeedback Extension*
