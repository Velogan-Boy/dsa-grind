# Last updated: 2/28/2026, 10:14:25 PM
from typing import List
from collections import defaultdict

class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def solve(start_even: bool):
            allowed = []
            ops = 0

            for i in range(n):
                expected_even = (i % 2 == 0) if start_even else (i % 2 == 1)
                if (nums[i] % 2 == 0) == expected_even:
                    allowed.append([nums[i]])
                else:
                    ops += 1
                    allowed.append([nums[i] - 1, nums[i] + 1])

            values = []
            for i in range(n):
                for v in allowed[i]:
                    values.append((v, i))

            values.sort()

            count = defaultdict(int)
            covered = 0
            left = 0
            best = float('inf')

            for right in range(len(values)):
                v, idx = values[right]
                count[idx] += 1
                if count[idx] == 1:
                    covered += 1

                while covered == n:
                    best = min(best, values[right][0] - values[left][0])
                    count[values[left][1]] -= 1
                    if count[values[left][1]] == 0:
                        covered -= 1
                    left += 1

            return ops, best

        op1, diff1 = solve(True)
        op2, diff2 = solve(False)

        if op1 < op2:
            return [op1, diff1]
        elif op2 < op1:
            return [op2, diff2]
        else:
            return [op1, min(diff1, diff2)]