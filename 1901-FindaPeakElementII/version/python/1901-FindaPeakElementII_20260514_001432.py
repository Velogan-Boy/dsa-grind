# Last updated: 5/14/2026, 12:14:32 AM
1class Solution:
2    def findPeakGrid(self, mat):
3        m, n = len(mat), len(mat[0])
4        s, e = 0, n - 1
5
6        while s <= e:
7            mid = (s + e) // 2
8            maxElement = float('-inf')
9            maxI = -1
10
11            for i in range(m):
12                if mat[i][mid] > maxElement:
13                    maxI = i
14                    maxElement = mat[i][mid]
15            
16            left = mat[maxI][mid - 1] if mid > 0 else -1
17            right = mat[maxI][mid + 1] if mid < n - 1 else -1
18
19            if mat[maxI][mid] > left and mat[maxI][mid] > right:
20                return [maxI,mid]
21            elif left > mat[maxI][mid]:
22                e = mid - 1
23            else:
24                s = mid + 1
25
26
27
28