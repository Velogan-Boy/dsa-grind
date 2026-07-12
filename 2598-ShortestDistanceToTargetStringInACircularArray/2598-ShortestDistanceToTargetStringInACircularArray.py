# Last updated: 7/12/2026, 6:16:04 PM
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: return 0
        n = len(words)

        i, j = startIndex + 1, startIndex - 1

        d = 0

        for _ in range(n):
            i%=n
            j%=n
            d+=1

            if words[i] == target or words[j] == target: return d

            i+=1
            j-=1

        return -1
        