# Last updated: 4/28/2026, 10:36:48 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3
4        maxCandy = max(candies)
5        res = [False] * len(candies)
6
7        for i, candy in enumerate(candies):
8            if candy + extraCandies >= maxCandy:
9                res[i] = True
10        
11        return res
12        