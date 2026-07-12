# Last updated: 7/12/2026, 6:19:36 PM
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        
        sorted_chars = freq.most_common()
        
        ans = []
        for char, count in sorted_chars:
            ans.append(char * count)
            
        return "".join(ans)