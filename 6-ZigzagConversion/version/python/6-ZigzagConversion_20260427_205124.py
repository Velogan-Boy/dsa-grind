# Last updated: 4/27/2026, 8:51:24 PM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5
6        rows = [""] * numRows
7        curr_row = 0
8        direction = 1  # 1 = down, -1 = up
9
10        for ch in s:
11            rows[curr_row] += ch
12
13            if curr_row == 0:
14                direction = 1
15            elif curr_row == numRows - 1:
16                direction = -1
17
18            curr_row += direction
19
20        return "".join(rows)