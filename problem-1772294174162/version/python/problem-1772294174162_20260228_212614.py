# Last updated: 2/28/2026, 9:26:14 PM
1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def makeParityAlternating(self, nums: List[int]) -> List[int]:
6        n = len(nums)
7
8        def solve(start_even: bool):
9            allowed = []
10            ops = 0
11
12            for i in range(n):
13                expected_even = (i % 2 == 0) if start_even else (i % 2 == 1)
14                if (nums[i] % 2 == 0) == expected_even:
15                    allowed.append([nums[i]])
16                else:
17                    ops += 1
18                    allowed.append([nums[i] - 1, nums[i] + 1])
19
20            values = []
21            for i in range(n):
22                for v in allowed[i]:
23                    values.append((v, i))
24
25            values.sort()
26
27            count = defaultdict(int)
28            covered = 0
29            left = 0
30            best = float('inf')
31
32            for right in range(len(values)):
33                v, idx = values[right]
34                count[idx] += 1
35                if count[idx] == 1:
36                    covered += 1
37
38                while covered == n:
39                    best = min(best, values[right][0] - values[left][0])
40                    count[values[left][1]] -= 1
41                    if count[values[left][1]] == 0:
42                        covered -= 1
43                    left += 1
44
45            return ops, best
46
47        op1, diff1 = solve(True)
48        op2, diff2 = solve(False)
49
50        if op1 < op2:
51            return [op1, diff1]
52        elif op2 < op1:
53            return [op2, diff2]
54        else:
55            return [op1, min(diff1, diff2)]