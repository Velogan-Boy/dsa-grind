# Last updated: 6/2/2026, 9:58:10 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3
4        n = len(coins)
5
6        @cache
7        def dfs(i, amount):
8            if amount == 0:
9                return 0
10
11            if i == n or amount < 0:
12                return float('inf')
13
14            take = 1 + dfs(i, amount - coins[i])
15            skip = dfs(i + 1, amount)
16
17            return min(take, skip)
18
19        ans = dfs(0, amount)
20
21        return ans if ans != float('inf') else -1