# Last updated: 5/24/2026, 12:26:11 AM
1class Solution:
2    def pacificAtlantic(self, heights):
3        if not heights:
4            return []
5        m, n = len(heights), len(heights[0])
6        directions = [(1,0), (-1,0), (0,1), (0,-1)]
7        
8        def dfs(i, j, visited):
9            visited.add((i, j))
10            for dx, dy in directions:
11                x, y = i + dx, j + dy
12                if 0 <= x < m and 0 <= y < n:
13                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
14                        dfs(x, y, visited)
15
16        pacific, atlantic = set(), set()
17        for j in range(n): dfs(0, j, pacific)
18        for i in range(m): dfs(i, 0, pacific)
19        for j in range(n): dfs(m-1, j, atlantic)
20        for i in range(m): dfs(i, n-1, atlantic)
21        return list(pacific & atlantic)