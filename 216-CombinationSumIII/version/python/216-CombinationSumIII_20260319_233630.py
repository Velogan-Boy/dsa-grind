# Last updated: 3/19/2026, 11:36:30 PM
1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        ans = []
4        nums = []
5        self.func(n, 1, nums, k, ans)
6        return ans
7
8
9    def func(self, sum, last, nums, k, ans):
10        if sum == 0 and len(nums) == k:
11            ans.append(list(nums))
12            return
13
14        if sum <= 0 or len(nums) > k:
15            return
16
17        for i in range(last, 10):
18            if i <= sum:
19                nums.append(i)
20                self.func(sum - i, i + 1, nums, k, ans)
21                nums.pop()
22            else:
23                break
24
25  