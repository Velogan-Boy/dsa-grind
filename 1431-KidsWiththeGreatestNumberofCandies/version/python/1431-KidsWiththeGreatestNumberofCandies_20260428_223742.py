# Last updated: 4/28/2026, 10:37:42 PM
1class Solution:
2    def kidsWithCandies(self, candies, extraCandies):
3
4        result = []
5        maxVal = max(candies)
6
7        for c in candies:
8            result.append(c + extraCandies >= maxVal)
9
10        return result