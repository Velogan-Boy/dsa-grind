# Last updated: 2/28/2026, 4:28:32 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0

        longest = 1
        st = set(nums)

        for num in st:
            if (num - 1) in st:
                continue
            else:
                inc = 1
                curr = 1
                while num + inc in st:
                    curr+=1
                    longest = max(curr, longest)
                    inc+=1
                


        return longest
        