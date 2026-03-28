# Last updated: 3/28/2026, 8:49:44 PM
1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        lsum, rsum = 0,0
4        
5        for i in range(k): lsum += cardPoints[i]
6
7        maxSum = lsum
8
9        rIndex = len(cardPoints) - 1
10        for i in range(k - 1, -1, -1):
11            lsum -= cardPoints[i]
12            rsum += cardPoints[rIndex]
13            rIndex -= 1
14
15            maxSum = max(maxSum, lsum + rsum)
16
17
18        return maxSum
19
20        