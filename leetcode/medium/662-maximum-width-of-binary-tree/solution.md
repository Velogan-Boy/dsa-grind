# Maximum Width of Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/1972920556/
- **Date:** 2026-04-08

## Solution

```python
from collections import deque
from math import inf

class Solution:
    def widthOfBinaryTree(self, root):
        q = deque([(root, 0)]) 
        ans = 0

        while q:
            size = len(q)
            _, first = q[0]
            _, last = q[-1]

            ans = max(ans, last - first + 1)

            for _ in range(size):
                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

        return ans
```

---
*Generated automatically by LeetFeedback Extension*
