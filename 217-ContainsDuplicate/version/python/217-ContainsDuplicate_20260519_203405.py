# Last updated: 5/19/2026, 8:34:05 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        last_seen = {}
4
5        for i, num in enumerate(nums):
6            if num in last_seen and i - last_seen[num] <= k:
7                return True
8            last_seen[num] = i
9
10        return False