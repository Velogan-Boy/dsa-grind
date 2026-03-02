# Last updated: 3/2/2026, 3:11:12 PM
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        hashSet = set(('a','e','i','o','u'))

        i = len(s) - 1

        while i >= 0 and s[i] in hashSet:
            s = s[:i] + '-' + s[i+1:]
            i-=1

        ans = ''

        for ch in s:
            if ch != '-': ans += ch

        return ans
                
        