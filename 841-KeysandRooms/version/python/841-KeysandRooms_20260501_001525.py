# Last updated: 5/1/2026, 12:15:25 AM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        # 0 -> n - 1
4        n = len(rooms)
5        visited = [0] * n
6
7        visited[0] = 1
8        q = deque([0])
9
10        while q:
11            node = q.popleft()
12
13            for nei in rooms[node]:
14                if not visited[nei]:
15                    visited[nei] = 1
16                    q.append(nei)
17        
18        return sum(visited) == n
19
20
21
22
23        
24
25        
26        