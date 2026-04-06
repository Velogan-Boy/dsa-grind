# Pre, Post, Inorder in one traversal

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/pre,-post,-inorder-in-one-traversal
- **Date:** 2026-04-06

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        
        pre = []
        ino = []
        post = []
        def helper(node):
            if not node: return

            pre.append(node.data)
            helper(node.left)
            ino.append(node.data)
            helper(node.right)
            post.append(node.data)

        helper(root)

        return [ino,pre,post]





```

---
*Generated automatically by LeetFeedback Extension*
