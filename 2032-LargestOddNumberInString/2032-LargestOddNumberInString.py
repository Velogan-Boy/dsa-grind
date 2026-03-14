# Last updated: 3/14/2026, 7:02:01 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in "13579":
                return num[:i+1]
        return ""