# Last updated: 7/12/2026, 6:16:50 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < k * m:
            return -1

        s = min(bloomDay)
        e = max(bloomDay)

        while s <= e:
            x = (s + e) // 2

            cnt = 0
            boquet = 0
            for i in range(n):
                if bloomDay[i] <= x:
                    cnt += 1
                else:
                    boquet += cnt // k
                    cnt = 0

            boquet += cnt // k

            if boquet >= m:
                e = x - 1
            else:
                s = x + 1

        return s

        