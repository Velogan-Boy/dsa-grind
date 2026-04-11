# Insert into a Binary Search Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1975170021/
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: return TreeNode(val)

        curr = root

        while curr:
            if curr.val < val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break

                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break

                curr = curr.left
            
        return root


        
```

---
*Generated automatically by LeetFeedback Extension*
