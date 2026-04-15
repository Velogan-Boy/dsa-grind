# Last updated: 4/15/2026, 9:24:54 PM
1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        if words[startIndex] == target: return 0
4        n = len(words)
5
6        i, j = startIndex + 1, startIndex - 1
7
8        d = 0
9
10        for _ in range(n):
11            i%=n
12            j%=n
13            d+=1
14
15            if words[i] == target or words[j] == target: return d
16
17            i+=1
18            j-=1
19
20        return -1
21        