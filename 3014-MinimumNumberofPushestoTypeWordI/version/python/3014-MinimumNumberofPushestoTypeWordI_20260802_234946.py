# Last updated: 8/2/2026, 11:49:46 PM
1from collections import defaultdict
2
3class Solution:
4    def minimumPushes(self, word: str) -> int:
5        freq = defaultdict(int)
6
7        for ch in word:
8            freq[ch] += 1
9
10        frequencies = sorted(freq.values(), reverse=True)
11
12        ans = 0
13        for i, f in enumerate(frequencies):
14            ans += f * (i // 8 + 1)
15
16        return ans