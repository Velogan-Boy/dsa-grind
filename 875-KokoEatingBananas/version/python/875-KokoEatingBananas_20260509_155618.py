# Last updated: 5/9/2026, 3:56:18 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low = 1
4        high = max(piles)
5
6        def reqHours(k):
7            hoursTaken = 0
8            for pile in piles:
9                hoursTaken += ceil(pile/k)
10
11            return hoursTaken
12            
13
14        while low <= high:
15            k = (low + high) // 2
16
17            if reqHours(k) <= h:
18                high = k - 1
19            else:
20                low = k + 1
21        
22        return low
23
24
25
26
27
28
29        