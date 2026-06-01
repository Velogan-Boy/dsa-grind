# Last updated: 6/1/2026, 11:52:40 PM
1class Solution:
2    def lengthOfLIS(self, nums):
3        tails = []
4
5        for num in nums:
6            left, right = 0, len(tails)
7
8            while left < right:
9                mid = (left + right) // 2
10
11                if tails[mid] < num:
12                    left = mid + 1
13                else:
14                    right = mid
15          
16            if left == len(tails):
17                tails.append(num)
18            else:
19                tails[left] = num
20
21        return len(tails)