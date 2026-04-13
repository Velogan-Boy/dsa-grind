# Last updated: 4/13/2026, 11:50:03 PM
1class Solution:
2    def cherryPickup(self, grid):
3        n = len(grid)
4        dp = {}
5
6        def dfs(r1, c1, r2):
7            c2 = r1 + c1 - r2
8            
9            if (r1 >= n or c1 >= n or 
10                r2 >= n or c2 >= n or
11                grid[r1][c1] == -1 or grid[r2][c2] == -1):
12                return float('-inf')
13            
14            if r1 == n-1 and c1 == n-1:
15                return grid[r1][c1]
16            
17            if (r1, c1, r2) in dp:
18                return dp[(r1, c1, r2)]
19            
20            cherries = 0
21            if r1 == r2 and c1 == c2:
22                cherries += grid[r1][c1]
23            else:
24                cherries += grid[r1][c1] + grid[r2][c2]
25            
26            best = max(
27                dfs(r1+1, c1, r2+1),  
28                dfs(r1, c1+1, r2),    
29                dfs(r1+1, c1, r2),    
30                dfs(r1, c1+1, r2+1)   
31            )
32            
33            cherries += best
34            dp[(r1, c1, r2)] = cherries
35            return cherries
36        
37        return max(0, dfs(0, 0, 0))