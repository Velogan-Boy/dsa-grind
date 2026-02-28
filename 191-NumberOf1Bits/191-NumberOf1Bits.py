# Last updated: 2/28/2026, 4:28:08 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
        