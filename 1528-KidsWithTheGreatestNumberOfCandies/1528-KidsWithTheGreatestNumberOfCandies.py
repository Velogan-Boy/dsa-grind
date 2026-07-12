# Last updated: 7/12/2026, 6:16:56 PM
class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        maxVal = max(candies)

        for c in candies:
            result.append(c + extraCandies >= maxVal)

        return result