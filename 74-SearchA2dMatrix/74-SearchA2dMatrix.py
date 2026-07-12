# Last updated: 7/12/2026, 6:23:58 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m,n = len(matrix), len(matrix[0])
        s, e = 0, m * n - 1

        while s <= e:
            mid = (s + e) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target: return True
            elif matrix[row][col] < target:
                s = mid + 1
            else:
                e = mid - 1

        return False


        