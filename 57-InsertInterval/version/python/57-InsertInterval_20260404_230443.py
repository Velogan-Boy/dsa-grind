# Last updated: 4/4/2026, 11:04:43 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3
4        res = []
5        i = 0
6        
7        n = len(intervals)
8        
9        while i < n and intervals[i][1] < newInterval[0]:
10            res.append(intervals[i])
11            i += 1
12        
13        while i < n and intervals[i][0] <= newInterval[1]:
14            newInterval[0] = min(newInterval[0], intervals[i][0])
15            newInterval[1] = max(newInterval[1], intervals[i][1])
16            i += 1
17        
18        res.append(newInterval)
19        
20        while i < n:
21            res.append(intervals[i])
22            i += 1
23        
24        return res
25
26        