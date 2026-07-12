# Last updated: 7/12/2026, 6:26:02 PM
class Solution:
    def myAtoi(self, s: str) -> int:

        def helper(s, i, started, sign, nums):

            if len(s) == i: return sign * nums

            c = s[i]

            if not started:
                if c == ' ':
                    return helper(s, i + 1, False, sign, nums)

                if c in '+-':
                    sign = -1 if c == '-' else 1
                    return helper(s, i + 1, True, sign, nums)
                
                if c.isdigit():
                    nums = int(c)
                    return helper(s, i + 1, True, sign, nums)

            else:
                if c.isdigit():
                    nums = (nums * 10) + int(c)
                    return helper(s, i + 1, True, sign, nums)

                else:
                    return sign * nums
                
        ans = helper(s, 0, False, 1, 0)

        if not ans: return 0

        if ans < -2**31:
            return -2**31
        if ans > 2**31 - 1:
            return 2**31 - 1
        
        return ans
        