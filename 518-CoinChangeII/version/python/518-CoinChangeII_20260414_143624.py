# Last updated: 4/14/2026, 2:36:24 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        n = len(coins)
4        memo = [[-1] * (amount + 1) for _ in range(n)]
5
6        def dfs(i, a):
7            if a == 0: return 1
8            if i < 0: return 0
9            if a < 0: return 0
10            
11            if memo[i][a] != -1: return memo[i][a]
12
13            pick = dfs(i, a - coins[i])
14            notPick = dfs(i - 1, a)
15
16            memo[i][a] = pick + notPick
17
18            return memo[i][a]
19
20
21        return dfs(n - 1, amount)
22
23       