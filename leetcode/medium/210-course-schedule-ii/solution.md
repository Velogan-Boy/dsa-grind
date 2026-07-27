# Course Schedule II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/course-schedule-ii/submissions/2083577985/
- **Date:** 2026-07-27

## Solution

```python
class Solution:
    def findOrder(self, V: int, pre: List[List[int]]) -> List[int]:
        graph=[[] for i in range(V)]

        for i,j in pre:
            graph[i].append(j)
            
        def dfs(root):
            path[root]=True 
            visited[root]=True
            for nei in graph[root]:
                if path[nei]:
                    return False 
                if visited[nei]:
                     continue
                if dfs(nei)==False:
                    return False 
            ans.append(root)
            path[root]=False 

        visited=[False for i in range(V)]
        path=[False for i in range(V)] 
        ans=[]

        for i in range(V):
            if not visited[i]:
                if dfs(i)==False:
                    return [] 
        return ans
```

---
*Generated automatically by LeetFeedback Extension*
