# Last updated: 5/1/2026, 10:17:11 PM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        m,n = len(image), len(image[0])
4
5        if image[sr][sc] == color:
6            return image
7
8        srcColor = image[sr][sc]
9        q = deque()
10        q.append((sr,sc))
11        visited = set((sr,sc))
12        image[sr][sc] = color
13
14        while q:
15            x, y = q.popleft()
16
17            for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
18                xx, yy = x + dx, y + dy
19
20                if xx < 0 or xx >= m or yy < 0 or yy >= n:
21                    continue
22                
23                if (xx,yy) in visited: continue
24
25                if image[xx][yy] == srcColor:
26                    image[xx][yy] = color
27                    visited.add((xx,yy))
28                    q.append((xx,yy))
29
30        return image
31
32
33
34
35
36
37
38
39        