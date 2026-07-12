# Last updated: 7/12/2026, 6:26:05 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = 1  # 1 = down, -1 = up

        for ch in s:
            rows[curr_row] += ch

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)