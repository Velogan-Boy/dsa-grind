# Last updated: 7/12/2026, 6:20:15 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        @cache
        def dfs(i, amount):
            if amount == 0:
                return 0

            if i == n or amount < 0:
                return float('inf')

            take = 1 + dfs(i, amount - coins[i])
            skip = dfs(i + 1, amount)

            return min(take, skip)

        ans = dfs(0, amount)

        return ans if ans != float('inf') else -1