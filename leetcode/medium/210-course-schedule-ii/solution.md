# Course Schedule II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/course-schedule-ii/submissions/2083589127/
- **Date:** 2026-07-27

## Solution

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        v = numCourses
        graph = [[] for _ in range(v)]

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(node):
            visited[node] = True
            path[node] = True

            for nei in graph[node]:
                if path[nei]: return False
                if visited[nei]: continue
                if dfs(nei) == False: return False

            path[node] = False
            stack.append(node)
            
        visited = [False] * v
        path = [False] * v
        stack = []

        for node in range(v):
            if visited[node]: continue

            if dfs(node) == False: return []
        
        return stack[::-1]





        

        
        
```

---
*Generated automatically by LeetFeedback Extension*
