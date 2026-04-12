# Last updated: 4/12/2026, 6:32:50 PM
1class Solution:
2    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
3        if len(nums) % k != 0:
4            return False
5
6        count = Counter(nums)
7        nums.sort()
8
9        for card in nums:
10            if count[card] == 0:
11                continue
12
13            for i in range(k):
14                if count[card + i] == 0:
15                    return False
16                count[card + i] -= 1
17
18        return True
19        