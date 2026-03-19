# Last updated: 3/19/2026, 11:47:09 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
4        ans = [] 
5        if not digits: return ans
6
7        def helper(index, current):
8            if index == len(digits):
9                ans.append(current)
10                return
11
12            s = map[int(digits[index])]
13
14            for char in s:
15                helper(index + 1, current + char)
16
17
18        helper(0, "")
19        return ans 
20
21