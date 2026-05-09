# Last updated: 5/9/2026, 4:30:36 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        n = len(bloomDay)
4        if n < k * m:
5            return -1
6
7        s = min(bloomDay)
8        e = max(bloomDay)
9
10        while s <= e:
11            x = (s + e) // 2
12
13            cnt = 0
14            boquet = 0
15            for i in range(n):
16                if bloomDay[i] <= x:
17                    cnt += 1
18                else:
19                    boquet += cnt // k
20                    cnt = 0
21
22            boquet += cnt // k
23
24            if boquet >= m:
25                e = x - 1
26            else:
27                s = x + 1
28
29        return s
30
31        