# Last updated: 3/5/2026, 7:04:29 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        if len(bloomDay) < k * m:
4            return -1
5
6        s = min(bloomDay)
7        e = max(bloomDay)
8
9        while s <= e:
10            x = (s + e) // 2
11
12            cnt = 0
13            boquet = 0
14            for i in range(len(bloomDay)):
15                if bloomDay[i] <= x:
16                    cnt += 1
17                else:
18                    boquet += cnt // k
19                    cnt = 0
20
21            boquet += cnt // k
22
23            if boquet >= m:
24                e = x - 1
25            else:
26                s = x + 1
27
28        return s
29
30        