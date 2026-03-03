# Last updated: 3/3/2026, 5:48:37 PM
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        cnt = 0
4        maxCnt = -inf
5        
6        for c in s:
7            if c == '(':
8                cnt += 1
9                maxCnt = max(cnt,maxCnt)
10            elif c == ')':
11                cnt -= 1
12
13        return maxCnt if maxCnt != -inf else 0
14
15        