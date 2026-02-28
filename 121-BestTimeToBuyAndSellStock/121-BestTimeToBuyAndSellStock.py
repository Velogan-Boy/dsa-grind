# Last updated: 2/28/2026, 4:28:40 PM
class Solution:
    def maxProfit(self, prices):
        left = 0  
        right = 1  
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
                
            right += 1

        return max_profit