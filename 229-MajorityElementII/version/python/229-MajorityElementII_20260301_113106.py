# Last updated: 3/1/2026, 11:31:06 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        if not nums:
4            return []
5
6        candidate1, candidate2, count1, count2 = None, None, 0, 0
7        for num in nums:
8            if candidate1 == num:
9                count1 += 1
10            elif candidate2 == num:
11                count2 += 1
12            elif count1 == 0:
13                candidate1, count1 = num, 1
14            elif count2 == 0:
15                candidate2, count2 = num, 1
16            else:
17                count1 -= 1
18                count2 -= 1
19
20        result = []
21        for c in [candidate1, candidate2]:
22            if c is not None and nums.count(c) > len(nums) // 3:
23                result.append(c)
24        return result