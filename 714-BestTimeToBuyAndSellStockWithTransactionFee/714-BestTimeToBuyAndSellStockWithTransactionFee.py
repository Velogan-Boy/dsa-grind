# Last updated: 2/27/2026, 5:21:43 PM
class Solution:
    def maxProfit(self, prices: List[int],fee:int) -> int:
        
        dp = [[-1,-1] for _ in range(len(prices))]

        return self.recRun(prices,0, 1,dp,fee)

    def recRun(self, prices, i , buy,dp,fee):

        if i == len(prices):
            return 0

        if dp[i][buy] != -1:
            return dp[i][buy]
        
        if buy == 1:
            dp[i][buy] = max(
                -prices[i] + self.recRun(prices,i + 1, 0,dp,fee),
                self.recRun(prices,i + 1, 1,dp,fee)
            )
        
        else:
            dp[i][buy] = max(
                +prices[i] - fee + self.recRun(prices,i + 1, 1,dp,fee),
                self.recRun(prices,i + 1, 0,dp,fee)
            )
        
        return dp[i][buy]

        
        