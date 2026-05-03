# Course Schedule

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/course-schedule/submissions/1994120839/
- **Date:** 2026-05-03

## Solution

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for a, b in prerequisites:
            adjList[b].append(a)
        
        visited = [0] * numCourses
        
        def dfs(node,visited):
            visited[node] = 1

            for nei in adjList[node]:
                if visited[nei] == 1:
                    return True

                if visited[nei] == 0:
                    if dfs(nei, visited):
                        return True
            
            visited[node] = 2
            return False

        for i in range(numCourses):
            if visited[i] != 2:
                if dfs(i, visited):
                    return False

        return True
            



            
            
                        


        


            

        
        
```

---
*Generated automatically by LeetFeedback Extension*
