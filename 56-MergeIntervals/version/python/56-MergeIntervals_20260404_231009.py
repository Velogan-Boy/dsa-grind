# Last updated: 4/4/2026, 11:10:09 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        if not intervals: return []
4
5        intervals.sort(key = lambda x : x[0])
6
7        merged = intervals[0:1]
8
9        for i in range(1, len(intervals)):
10            if merged[-1][1] >= intervals[i][0]:
11                merged[-1][0] = min(merged[-1][0], intervals[i][0])
12                merged[-1][1] = max(merged[-1][1], intervals[i][1])
13            else:
14                merged.append(intervals[i])
15
16        return merged
17
18
19
20
21        