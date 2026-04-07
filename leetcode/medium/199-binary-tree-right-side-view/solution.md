# Binary Tree Right Side View

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-tree-right-side-view/submissions/1971804544/
- **Date:** 2026-04-07

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque([root])
        ans = []

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

                if i == size - 1:
                    ans.append(curr.val)
        return ans
                







        
```

---
*Generated automatically by LeetFeedback Extension*
