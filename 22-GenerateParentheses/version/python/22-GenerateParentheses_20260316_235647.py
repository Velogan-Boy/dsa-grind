# Last updated: 3/16/2026, 11:56:47 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        def dfs(left, right, s):
4            if len(s) == n * 2:
5                res.append(s)
6                return 
7
8            if left < n:
9                dfs(left + 1, right, s + '(')
10
11            if right < left:
12                dfs(left, right + 1, s + ')')
13
14        res = []
15        dfs(0, 0, '')
16        return res
17        