# Last updated: 7/14/2026, 11:14:52 PM
1class Solution:
2    def snakesAndLadders(self, board: List[List[int]]) -> int:
3        n = len(board)
4
5        def getPos(num):
6            r = (num - 1) // n
7            c = (num - 1) % n
8
9            if r % 2 == 1:
10                c = n - 1 - c
11
12            r = n - 1 - r
13
14            return (r,c)
15
16        q = deque()
17        q.append((1, 0))
18        visited = set()
19        visited.add(1)
20
21        while q:
22            curr, moves = q.popleft()
23
24            if curr == n * n: return moves
25
26            for dice in range(1, 7):
27                next = curr + dice
28
29                if next > n * n: break
30
31                r,c = getPos(next)
32
33                if board[r][c] != -1:
34                    next = board[r][c]
35
36                if next in visited: continue
37
38                q.append((next, moves + 1))
39                visited.add(next)
40            
41
42        return -1
43
44
45        
46
47
48
49        