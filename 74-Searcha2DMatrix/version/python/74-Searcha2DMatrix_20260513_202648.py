# Last updated: 5/13/2026, 8:26:48 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3
4        m,n = len(matrix), len(matrix[0])
5        s, e = 0, m * n - 1
6
7        while s <= e:
8            mid = (s + e) // 2
9            row = mid // n
10            col = mid % n
11
12            if matrix[row][col] == target: return True
13            elif matrix[row][col] < target:
14                s = mid + 1
15            else:
16                e = mid - 1
17
18        return False
19
20
21        