# Last updated: 2/28/2026, 4:27:32 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s) -1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1
        