# Last updated: 3/5/2026, 11:30:03 PM
1class Solution:
2    def findKthPositive(self, arr: List[int], k: int) -> int:
3        s = 0
4        e = len(arr) - 1
5
6        while s <= e:
7            mid = (s + e) // 2
8
9            missing = arr[mid] - (mid + 1)
10
11            if missing < k:
12                s = mid + 1
13            else:
14                e = mid - 1
15
16        return s + k
17
18
19
20        