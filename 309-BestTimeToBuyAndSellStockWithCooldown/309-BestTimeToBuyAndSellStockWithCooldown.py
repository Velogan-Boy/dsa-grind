# Last updated: 2/27/2026, 10:35:19 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[-1,-1] for _ in range(len(prices))]

        return self.recRun(prices,0, 1,dp)

    def recRun(self, prices, i , buy,dp):

        if i >= len(prices):
            return 0

        if dp[i][buy] != -1:
            return dp[i][buy]
        
        if buy == 1:
            dp[i][buy] = max(
                -prices[i] + self.recRun(prices,i + 1, 0,dp),
                self.recRun(prices,i + 1, 1,dp)
            )
        
        else:
            dp[i][buy] = max(
                +prices[i] + self.recRun(prices,i + 2, 1,dp),
                self.recRun(prices,i + 1, 0,dp)
            )
        
        return dp[i][buy]

        
        