# Last updated: 2/28/2026, 4:26:20 PM
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) < N - 1:
            return -1

        if not trust:
            return 1

        trust_scores = [0] * (N+1)

        for a,b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i,score in enumerate(trust_scores):

            if score == N - 1:
                return i

        return -1