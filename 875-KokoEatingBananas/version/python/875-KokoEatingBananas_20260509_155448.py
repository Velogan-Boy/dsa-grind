# Last updated: 5/9/2026, 3:54:48 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        piles.sort()
4
5        low = 1
6        high = piles[-1]
7
8        def reqHours(k):
9            hoursTaken = 0
10            for pile in piles:
11                hoursTaken += ceil(pile/k)
12
13            return hoursTaken
14            
15
16        while low <= high:
17            mid = (low + high) // 2
18
19            if reqHours(mid) <= h:
20                ans = mid
21                high = mid - 1
22            else:
23                low = mid + 1
24        
25        return ans
26
27
28
29
30
31
32        