# Last updated: 7/12/2026, 6:18:08 PM
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




        

        
        