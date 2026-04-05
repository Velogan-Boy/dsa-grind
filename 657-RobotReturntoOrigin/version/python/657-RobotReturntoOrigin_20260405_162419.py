# Last updated: 4/5/2026, 4:24:19 PM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        
4        dMap = { "U": [0,1], "R": [1,0], "D": [0, -1], "L": [-1, 0] }
5
6        origin = [0,0]
7        for d in moves:
8            origin[0] += dMap[d][0]
9            origin[1] += dMap[d][1]
10
11        return origin == [0,0]
12
13
14        