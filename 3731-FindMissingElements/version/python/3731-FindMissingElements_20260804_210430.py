# Last updated: 8/4/2026, 9:04:30 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3
4        mini = min(nums)
5        maxi = max(nums)
6
7        hashSet = set(nums)
8
9        ans = []
10        for num in range(mini, maxi + 1):
11            if num not in hashSet:
12                ans.append(num)
13
14        return ans
15
16
17
18        