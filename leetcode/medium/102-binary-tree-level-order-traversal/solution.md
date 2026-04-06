# Binary Tree Level Order Traversal

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1970402756/
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            ans = []

            if not root: return ans

            queue = []

            queue.append(root)

            while queue:
                level = []

                for _i in range(len(queue)):
                    node = queue.pop(0)
                    level.append(node.val)

                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                
                ans.append(level)

            

            return ans
            










        
```

---
*Generated automatically by LeetFeedback Extension*
