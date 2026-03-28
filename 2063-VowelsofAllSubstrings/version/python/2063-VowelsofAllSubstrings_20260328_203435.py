# Last updated: 3/28/2026, 8:34:35 PM
1class Solution:
2    def countVowels(self, word: str) -> int:
3        n = len(word)
4        count = 0
5
6        for i in range(n):
7            if word[i] in 'aeiou':
8                count += (n - i) * (i + 1)
9
10        return count                
11        