# Last updated: 3/1/2026, 8:11:10 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4
5        merged = []
6
7        for interval in intervals:
8            if not merged or merged[-1][1] < interval[0]:
9                merged.append(interval)
10            else:
11                merged[-1][1] = max(
12                    merged[-1][1],
13                    interval[1]
14                )
15
16        return merged
17
18