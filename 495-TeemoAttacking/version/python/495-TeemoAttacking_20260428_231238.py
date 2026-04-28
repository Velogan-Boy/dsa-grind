# Last updated: 4/28/2026, 11:12:38 PM
1class Solution:
2    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
3        if duration == 0: return 0
4
5        res = 0
6        for i in range(len(timeSeries)):
7            if i != len(timeSeries) - 1:
8                res += min(duration, timeSeries[i + 1] - timeSeries[i])
9            else:
10                res += duration
11
12        return res
13            
14
15        