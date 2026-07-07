# Last updated: 7/7/2026, 11:56:11 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        word_set = set(wordDict)
4        n = len(s)
5        dp = [True] * (n + 1)
6
7        def breaks(st):
8            # If we already know this starting index is a dead end, skip it!
9            if not dp[st]:
10                return False
11
12            for i in range(st, n):
13                word = s[st:i+1]
14                if word in word_set:
15                    if i == n - 1:
16                        return True
17                    if i < n - 1 and breaks(i + 1):
18                        return True
19            
20            # Mark this index as a dead end for future recursive calls
21            dp[st] = False
22            return False
23
24        return breaks(0)