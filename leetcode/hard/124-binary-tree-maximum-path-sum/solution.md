# Binary Tree Maximum Path Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1970495927/
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(node, maxPathSum):
            if not node: return 0

            left = max(0, helper(node.left, maxPathSum))
            right = max(0, helper(node.right, maxPathSum))

            maxPathSum[0] = max(maxPathSum[0], left + right + node.val)

            return max(left,right) + node.val

        maxPathSum = [-inf]
        helper(root,maxPathSum)

        return maxPathSum[0]
        
        
```

---
*Generated automatically by LeetFeedback Extension*
