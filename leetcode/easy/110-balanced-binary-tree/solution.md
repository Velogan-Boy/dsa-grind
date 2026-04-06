# Balanced Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/balanced-binary-tree/submissions/1970470217/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node, isBalanced):
            if not node: return 0

            left = helper(node.left, isBalanced) + 1
            right = helper(node.right, isBalanced) + 1

            if abs(left - right) > 1: isBalanced[0] = False

            return max(left, right)

        isBalanced = [True]

        helper(root, isBalanced)

        return isBalanced[0]


        
```

---
*Generated automatically by LeetFeedback Extension*
