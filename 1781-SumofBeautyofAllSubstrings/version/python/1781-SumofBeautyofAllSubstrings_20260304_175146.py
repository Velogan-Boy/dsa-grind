# Last updated: 3/4/2026, 5:51:46 PM
1class Solution:
2    def beautySum(self, s: str) -> int:
3        n = len(s)
4        total_beauty = 0
5        for i in range(n):
6            freq = {}
7            for j in range(i,n):
8                freq[s[j]] = freq.get(s[j], 0) + 1
9                maxf = max(freq.values())
10                minf = min(freq.values())
11                total_beauty += maxf - minf
12        return total_beauty