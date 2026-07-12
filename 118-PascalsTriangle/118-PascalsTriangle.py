# Last updated: 7/12/2026, 6:22:50 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            currRow = [0] * (i + 1)

            for j in range(i + 1):
                if j == 0 or j == i:
                    currRow[j] = 1
                else:
                    currRow[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            
            ans.append(currRow)

        return ans



        