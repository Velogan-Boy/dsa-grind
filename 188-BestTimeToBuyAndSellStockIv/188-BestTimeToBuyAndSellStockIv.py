# Last updated: 2/27/2026, 5:22:09 PM
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(len(prices))]

        return self.recRun(prices, 0, 1, k,dp)

    def recRun(self, prices, i , buy, cap,dp):

        if cap <= 0: return 0

        if i == len(prices): return 0

        if dp[i][buy][cap] != -1: return dp[i][buy][cap]

        if buy == 1:
            dp[i][buy][cap] = max(-prices[i] + self.recRun(prices, i + 1, 0, cap,dp),
                        0 + self.recRun(prices,i + 1, 1, cap,dp) )

        else:
            dp[i][buy][cap] = max(+prices[i] + self.recRun(prices, i + 1, 1, cap - 1,dp),
                        self.recRun(prices, i + 1, 0, cap,dp))

        return dp[i][buy][cap]



        
        