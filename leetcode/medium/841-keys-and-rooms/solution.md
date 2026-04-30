# Keys and Rooms

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/keys-and-rooms/submissions/1992058877/
- **Date:** 2026-04-30

## Solution

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 0 -> n - 1
        n = len(rooms)
        visited = [0] * n

        visited[0] = 1
        q = deque([0])

        while q:
            node = q.popleft()

            for nei in rooms[node]:
                if not visited[nei]:
                    visited[nei] = 1
                    q.append(nei)
        
        return sum(visited) == n




        

        
        
```

---
*Generated automatically by LeetFeedback Extension*
