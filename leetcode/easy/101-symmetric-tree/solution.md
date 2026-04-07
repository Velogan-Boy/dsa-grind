# Symmetric Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/symmetric-tree/description/
- **Date:** 2026-04-07

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isSymmetric(self, root):

        def isSameTree(p,q):
            if not p and not q: return True
            if not p or not q: return False

            return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left, root.right)
        
        
```

---
*Generated automatically by LeetFeedback Extension*
