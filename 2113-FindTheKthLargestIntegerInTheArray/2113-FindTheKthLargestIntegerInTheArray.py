# Last updated: 2/27/2026, 5:11:04 PM
from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num_list = [int(num) for num in nums]

        num_list.sort()

        kth_largest = num_list[len(num_list) - k]

        return str(kth_largest)