# Last updated: 4/27/2026, 8:47:56 PM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5
6        res = ""
7        n = len(s)
8        increment = 2 * (numRows - 1)
9
10        for row in range(numRows):
11            for i in range(row, n, increment):
12                res += s[i]
13
14                if row != 0 and row != numRows - 1:
15                    diag = i + increment - 2 * row
16                    if diag < n:
17                        res += s[diag]
18
19        return res