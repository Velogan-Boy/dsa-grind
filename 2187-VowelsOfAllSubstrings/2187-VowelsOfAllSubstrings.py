# Last updated: 7/12/2026, 6:16:19 PM
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0

        for i in range(n):
            if word[i] in 'aeiou':
                count += (n - i) * (i + 1)

        return count                
        