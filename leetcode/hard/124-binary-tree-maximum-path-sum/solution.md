# Binary Tree Maximum Path Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/2015755190/
- **Date:** 2026-05-28

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        globalMax = float('-inf')

        def dfs(node):
            nonlocal globalMax

            if not node:
                return 0

            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            globalMax = max(globalMax, l + r + node.val)

            return node.val + max(l, r)

        dfs(root)

        return globalMax
```

---
*Generated automatically by LeetFeedback Extension*
