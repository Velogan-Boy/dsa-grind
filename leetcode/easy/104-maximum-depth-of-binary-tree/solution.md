# Maximum Depth of Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1970452223/
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node: return 0

            return max(helper(node.left), helper(node.right)) + 1

        return helper(root)
        
```

---
*Generated automatically by LeetFeedback Extension*
