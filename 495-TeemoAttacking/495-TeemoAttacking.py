# Last updated: 7/12/2026, 6:19:30 PM
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0

        res = 0
        for i in range(len(timeSeries)):
            if i != len(timeSeries) - 1:
                res += min(duration, timeSeries[i + 1] - timeSeries[i])
            else:
                res += duration

        return res
            

        