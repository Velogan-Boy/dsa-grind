# Last updated: 7/12/2026, 6:25:42 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [] 
        if not digits: return ans

        def helper(index, current):
            if index == len(digits):
                ans.append(current)
                return

            s = map[int(digits[index])]

            for char in s:
                helper(index + 1, current + char)


        helper(0, "")
        return ans 

