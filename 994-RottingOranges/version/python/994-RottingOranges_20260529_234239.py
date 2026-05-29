# Last updated: 5/29/2026, 11:42:39 PM
1from collections import deque
2
3class Solution:
4    def orangesRotting(self, grid: List[List[int]]) -> int:
5        rows = len(grid)
6        if rows == 0: 
7            return -1
8        
9        cols = len(grid[0])
10        
11        fresh_cnt = 0
12        
13        rotten = deque()
14        
15        for r in range(rows):
16            for c in range(cols):
17                if grid[r][c] == 2:
18                    rotten.append((r, c))
19                elif grid[r][c] == 1:
20                    fresh_cnt += 1
21        
22        minutes_passed = 0
23        
24        while rotten and fresh_cnt > 0:
25
26            minutes_passed += 1
27            
28            for _ in range(len(rotten)):
29                x, y = rotten.popleft()
30                
31                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
32                    xx, yy = x + dx, y + dy
33                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
34                        continue
35
36                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
37                        continue
38                        
39                    fresh_cnt -= 1
40                    grid[xx][yy] = 2
41                    
42                    rotten.append((xx, yy))
43
44        
45        return minutes_passed if fresh_cnt == 0 else -1