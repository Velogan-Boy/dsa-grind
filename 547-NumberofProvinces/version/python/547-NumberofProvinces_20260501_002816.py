# Last updated: 5/1/2026, 12:28:16 AM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        visited = set()
5
6        def dfs(city):
7            for nei in range(n):
8                if isConnected[city][nei] == 1 and nei not in visited:
9                    visited.add(nei)
10                    dfs(nei)
11
12        provinces = 0
13
14        for i in range(n):
15            if i not in visited:
16                visited.add(i)
17                dfs(i)
18                provinces += 1
19
20        return provinces
21
22            
23            