# Last updated: 2/27/2026, 5:19:41 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m = len(prices)

        curr = [0,0]
        ahead = [0,0]

        for i in range(m - 1, -1, -1):
            for buy in range(0, 2):
                if buy == 1:
                    curr[buy] = max(
                        -prices[i] + ahead[0],
                        ahead[1],
                    )

                else:
                    curr[buy] = max(
                        +prices[i] + ahead[1],
                        ahead[0]
                    )

            ahead = curr  

        return ahead[1]