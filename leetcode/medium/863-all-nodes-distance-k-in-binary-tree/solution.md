# All Nodes Distance K in Binary Tree

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/1972943889/
- **Date:** 2026-04-08

## Solution

```python
class Solution:
    def distanceK(self, root, target, k):
        pm = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                pm[node.left] = node
                queue.append(node.left)
            if node.right:
                pm[node.right] = node
                queue.append(node.right)

        result = []
        visited = set()
        queue = deque([target])
        visited.add(target)
        d = 0

        while queue:
            if d == k:
                result.extend(node.val for node in queue)
                return result

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                if node in pm and pm[node] not in visited:
                    visited.add(pm[node])
                    queue.append(pm[node])

            d += 1

        return result


```

---
*Generated automatically by LeetFeedback Extension*
