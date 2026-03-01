# Last updated: 3/1/2026, 10:59:07 AM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        ans = []
4        for i in range(numRows):
5            currRow = [0] * (i + 1)
6
7            for j in range(i + 1):
8                if j == 0 or j == i:
9                    currRow[j] = 1
10                else:
11                    currRow[j] = ans[i - 1][j - 1] + ans[i - 1][j]
12            
13            ans.append(currRow)
14
15        return ans
16
17
18
19        