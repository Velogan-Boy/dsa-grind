# Last updated: 5/22/2026, 7:59:46 PM
1class Solution:
2    def zeroFilledSubarray(self, nums: List[int]) -> int:
3        i , j = 0, 0
4        count = 0
5        n = len(nums)
6
7        while i < n and j < n:
8            while i < n and nums[i] != 0 and i < n: i += 1
9            j = i + 1
10
11            if i >= n: break
12
13            while j < n and nums[j] == 0: j += 1
14
15            l = j - i
16
17            count += l * (l + 1) // 2
18
19            i = j + 1
20
21        return count
22
23
24
25
26
27
28
29
30        