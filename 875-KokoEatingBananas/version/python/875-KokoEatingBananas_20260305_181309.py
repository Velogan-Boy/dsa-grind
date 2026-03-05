# Last updated: 3/5/2026, 6:13:09 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        totalBananas = sum(piles)
4        if not totalBananas: return 0
5
6        s = 1
7        e = max(piles)
8
9        while s <= e:
10            k = (s + e) // 2
11
12            hour = 0
13            for i in range(len(piles)):
14                hour += math.ceil(piles[i] / k)
15            
16            if hour <= h: 
17                e = k - 1
18            else: s = k + 1
19    
20           
21        return s