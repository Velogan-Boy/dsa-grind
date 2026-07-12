# Last updated: 7/12/2026, 6:22:02 PM
class Solution:
    def maxProduct(self, arr):
        n = len(arr)

        pre, suff = 1, 1

        ans = float('-inf')

        for i in range(n):
            if pre == 0:
                pre = 1

            if suff == 0:
                suff = 1

            pre *= arr[i]

            suff *= arr[n - i - 1]

            ans = max(ans, pre, suff)

        return ans
