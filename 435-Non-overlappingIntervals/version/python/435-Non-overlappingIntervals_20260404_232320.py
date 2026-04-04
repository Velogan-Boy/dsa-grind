# Last updated: 4/4/2026, 11:23:20 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        
4        intervals.sort(key=lambda x: x[1])
5        n = len(intervals)
6
7        cnt = 1
8
9        lastEndTime = intervals[0][1]
10
11        for i in range(1, n):
12            if intervals[i][0] >= lastEndTime:
13                cnt += 1
14                lastEndTime = intervals[i][1]
15
16        return n - cnt
17
18        