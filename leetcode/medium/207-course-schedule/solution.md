# Course Schedule

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/course-schedule/submissions/1994116607/
- **Date:** 2026-05-03

## Solution

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        # b -> a
        for a, b in prerequisites:
            adjList[b].append(a)
        
        visited = set()
        pathVisited = set()
        
        def dfs(node,visited, pathVisited):
            visited.add(node)
            pathVisited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    if dfs(nei, visited, pathVisited):
                        return True
                else:
                    if nei in pathVisited: 
                        return True
            
            pathVisited.remove(node)
            return False

        for i in range(numCourses):
            if i not in visited:
                if dfs(i, visited, pathVisited):
                    return False

        return True
            



            
            
                        


        


            

        
        
```

---
*Generated automatically by LeetFeedback Extension*
