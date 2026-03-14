# Last updated: 3/14/2026, 7:02:10 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxCnt = -inf
        
        for c in s:
            if c == '(':
                cnt += 1
                maxCnt = max(cnt,maxCnt)
            elif c == ')':
                cnt -= 1

        return maxCnt if maxCnt != -inf else 0

        