# Construct Binary Search Tree from Preorder Traversal

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/submissions/1975219081/
- **Date:** 2026-04-11

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, A):
        i = 0
        
        def helper(A, bound):
            nonlocal i
            if i == len(A) or A[i] > bound: return None

            node = TreeNode(A[i])
            i+=1
            node.left = helper(A,node.val)
            node.right = helper(A, bound)

            return node
            
        return helper(A, inf)
        
```

---
*Generated automatically by LeetFeedback Extension*
