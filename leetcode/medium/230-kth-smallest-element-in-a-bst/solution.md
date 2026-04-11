# Kth Smallest Element in a BST

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1975191986/
- **Date:** 2026-04-11

## Solution

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1
        ans = -1

        def inorderTraverse(node):
            nonlocal ans
            nonlocal i

            if not node: return

            inorderTraverse(node.left)
            if i == k: ans = node.val
            i+=1
            inorderTraverse(node.right)
        
        inorderTraverse(root)
        return ans
```

---
*Generated automatically by LeetFeedback Extension*
