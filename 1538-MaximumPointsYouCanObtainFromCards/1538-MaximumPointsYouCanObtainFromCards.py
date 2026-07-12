# Last updated: 7/12/2026, 6:16:55 PM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum = 0,0
        
        for i in range(k): lsum += cardPoints[i]

        maxSum = lsum

        rIndex = len(cardPoints) - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rIndex]
            rIndex -= 1

            maxSum = max(maxSum, lsum + rsum)


        return maxSum

        