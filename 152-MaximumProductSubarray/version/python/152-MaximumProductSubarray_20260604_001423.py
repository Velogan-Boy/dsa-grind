# Last updated: 6/4/2026, 12:14:23 AM
1class Solution:
2    def maxProduct(self, arr):
3        n = len(arr)
4
5        pre, suff = 1, 1
6
7        ans = float('-inf')
8
9        for i in range(n):
10            if pre == 0:
11                pre = 1
12
13            if suff == 0:
14                suff = 1
15
16            pre *= arr[i]
17
18            suff *= arr[n - i - 1]
19
20            ans = max(ans, pre, suff)
21
22        return ans
23