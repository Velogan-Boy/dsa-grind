# Last updated: 7/13/2026, 11:22:32 AM
1class Solution:
2    def countValidWords(self, sentence: str) -> int:
3
4        def valid(word):
5            hyphen = 0
6
7            for i, ch in enumerate(word):
8
9                if ch.isdigit():
10                    return False
11
12                if ch in "!.,":
13                    if i != len(word) - 1:
14                        return False
15
16                elif ch == '-':
17                    hyphen += 1
18
19                    if hyphen > 1:
20                        return False
21
22                    if (
23                        i == 0 or
24                        i == len(word) - 1 or
25                        not word[i-1].islower() or
26                        not word[i+1].islower()
27                    ):
28                        return False
29
30            return True
31
32        ans = 0
33
34        for word in sentence.split():
35            if valid(word):
36                ans += 1
37
38        return ans