# Last updated: 4/3/2026, 7:10:21 PM
1class Solution:
2    def candy(self, ratings: List[int]) -> int:
3
4        n = len(ratings)
5
6        left = [1] * n
7
8        for i in range(1, n):
9            if ratings[i] > ratings[i - 1]:
10                left[i] = left[i - 1] + 1
11        
12        right = 1
13        ans = max(1, left[n-1])
14        
15        for i in range(n - 2, -1, -1):
16            if ratings[i] > ratings[i + 1]:
17                curr = right + 1
18            else:
19                curr = 1
20            
21            right = curr
22            
23            ans += max(curr, left[i])
24
25        return ans
26
27
28
29
30        