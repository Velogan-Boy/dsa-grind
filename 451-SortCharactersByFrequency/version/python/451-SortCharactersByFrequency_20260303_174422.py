# Last updated: 3/3/2026, 5:44:22 PM
1from collections import Counter
2
3class Solution:
4    def frequencySort(self, s: str) -> str:
5        freq = Counter(s)
6        
7        sorted_chars = freq.most_common()
8        
9        ans = []
10        for char, count in sorted_chars:
11            ans.append(char * count)
12            
13        return "".join(ans)