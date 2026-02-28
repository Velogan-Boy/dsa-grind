# Last updated: 2/28/2026, 4:25:14 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3
4        if not nums: return 0
5
6        longest = 1
7        st = set(nums)
8
9        for num in st:
10            if (num - 1) in st:
11                continue
12            else:
13                inc = 1
14                curr = 1
15                while num + inc in st:
16                    curr+=1
17                    longest = max(curr, longest)
18                    inc+=1
19                
20
21
22        return longest
23        