# Binary Tree Zigzag Level Order Traversal

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1970502039/
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = deque([root])
        zigZag = []
        direction = 1

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            zigZag.append(level[::direction])
            direction = -direction
        
        return zigZag






        
        
```

---
*Generated automatically by LeetFeedback Extension*
