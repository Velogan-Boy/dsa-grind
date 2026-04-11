# Maximum Sum BST in Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/solutions/
- **Date:** 2026-04-11

## Solution

```python
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return inf, -inf, 0
            
            lmin,lmax,lsum = dfs(node.left)
            rmin,rmax,rsum = dfs(node.right)

            if lmax < node.val < rmin:
                currSum = lsum + rsum + node.val
                ans = max(ans, currSum)

                return min(node.val, lmin), max(node.val, rmax), currSum

            else:
                return -inf, inf, 0
        
        dfs(root)

        return ans

            
        
```

---
*Generated automatically by LeetFeedback Extension*
