# Last updated: 4/4/2026, 10:41:19 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3
4        if not intervals: return [newInterval]
5
6        merged = []
7
8        inserted = 0
9        for start,end  in intervals:
10            if start > newInterval[0] and inserted == 0:
11                merged.append(newInterval)
12                inserted = 1
13            
14            merged.append([start,end])
15
16        if inserted == 0: merged.append(newInterval)
17
18        ans = merged[0:1]
19        for i in range(1, len(merged)):
20            if ans[-1][1] >= merged[i][0]:
21                ans[-1][0] = min(ans[-1][0], merged[i][0]) 
22                ans[-1][1] = max(ans[-1][1], merged[i][1])  
23            else:
24                ans.append(merged[i])
25
26
27        return ans
28            
29
30        