# Last updated: 7/12/2026, 6:16:28 PM
class Solution:
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        s, e = 0, n - 1

        while s <= e:
            mid = (s + e) // 2
            maxElement = float('-inf')
            maxI = -1

            for i in range(m):
                if mat[i][mid] > maxElement:
                    maxI = i
                    maxElement = mat[i][mid]
            
            left = mat[maxI][mid - 1] if mid > 0 else -1
            right = mat[maxI][mid + 1] if mid < n - 1 else -1

            if mat[maxI][mid] > left and mat[maxI][mid] > right:
                return [maxI,mid]
            elif left > mat[maxI][mid]:
                e = mid - 1
            else:
                s = mid + 1



