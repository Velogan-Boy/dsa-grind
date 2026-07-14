# Last updated: 7/14/2026, 10:33:26 PM
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
13            return r, c
14
15        q = deque([(1, 0)])
16        visited = {1}
17
18        while q:
19            square, moves = q.popleft()
20
21            if square == n * n:
22                return moves
23
24            for dice in range(1, 7):
25                nxt = square + dice
26
27                if nxt > n * n:
28                    break
29
30                r, c = getPos(nxt)
31
32                if board[r][c] != -1:
33                    nxt = board[r][c]
34
35                if nxt not in visited:
36                    visited.add(nxt)
37                    q.append((nxt, moves + 1))
38
39        return -1