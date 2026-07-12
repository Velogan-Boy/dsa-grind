# Last updated: 7/12/2026, 6:16:10 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        n = start ^ goal

        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt += 1

        return cnt

        