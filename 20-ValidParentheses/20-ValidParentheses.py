# Last updated: 7/12/2026, 6:25:36 PM
class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {'}': '{', ')': '(', ']':'['}
        stack = []

        for ch in s:
            if stack and ch in hashMap and stack[-1] == hashMap[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return not stack
            

        