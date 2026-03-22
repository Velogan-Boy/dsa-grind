# Last updated: 3/22/2026, 2:01:47 PM
1from collections import defaultdict
2
3class Solution:
4    def duplicateNumbersXOR(self, nums):
5        freq = defaultdict(int)
6        xor = 0
7        for num in nums:
8            freq[num] += 1
9            if freq[num] == 2:
10                xor ^= num
11        return xor