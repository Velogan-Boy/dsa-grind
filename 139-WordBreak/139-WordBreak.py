# Last updated: 7/12/2026, 6:22:15 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [True] * (n + 1)

        def breaks(st):
            # If we already know this starting index is a dead end, skip it!
            if not dp[st]:
                return False

            for i in range(st, n):
                word = s[st:i+1]
                if word in word_set:
                    if i == n - 1:
                        return True
                    if i < n - 1 and breaks(i + 1):
                        return True
            
            # Mark this index as a dead end for future recursive calls
            dp[st] = False
            return False

        return breaks(0)