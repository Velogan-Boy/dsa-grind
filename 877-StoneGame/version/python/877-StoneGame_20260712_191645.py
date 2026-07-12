# Last updated: 7/12/2026, 7:16:45 PM
1class Solution:
2    def stoneGame(self, piles: List[int]) -> bool:
3
4        # max advantage i can have over other player in the subarry piles[l, r]
5        @cache
6        def dfs(l, r): 
7            if l == r: return piles[l]
8
9            pickStart = piles[l] - dfs(l+1,r)
10            pickEnd = piles[r] - dfs(l, r-1)
11
12            return max(pickStart, pickEnd)
13
14        return dfs(0, len(piles) - 1) >= 1
15
16        