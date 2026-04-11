# Delete Node in a BST

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-node-in-a-bst/submissions/1975182392/
- **Date:** 2026-04-11

## Solution

```python
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
```

---
*Generated automatically by LeetFeedback Extension*
