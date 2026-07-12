# Last updated: 7/12/2026, 6:16:44 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        e = len(arr) - 1

        while s <= e:
            mid = (s + e) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                s = mid + 1
            else:
                e = mid - 1

        return s + k



        