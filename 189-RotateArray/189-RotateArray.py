# Last updated: 2/27/2026, 5:03:19 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]