# Last updated: 5/11/2026, 1:12:12 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3
4        count = defaultdict(int)
5        n = len(nums)
6        ans = set()
7
8        for num in nums:
9            count[num] += 1
10
11            if count[num] > n // 3:
12                ans.add(num)
13            
14        return list(ans)
15
16
17
18
19        