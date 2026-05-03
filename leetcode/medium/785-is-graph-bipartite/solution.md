# Is Graph Bipartite?

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/is-graph-bipartite/
- **Date:** 2026-05-03

## Solution

```python
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node: int, c: int):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - c):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
```

---
*Generated automatically by LeetFeedback Extension*
