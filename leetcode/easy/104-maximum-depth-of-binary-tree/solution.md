# Maximum Depth of Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/2009288255/
- **Date:** 2026-05-21

## Solution

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 0
        
        while q:
            depth += 1
            
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return depth        
```

---
*Generated automatically by LeetFeedback Extension*
