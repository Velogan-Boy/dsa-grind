# Snakes and Ladders

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/snakes-and-ladders/submissions/2067656121/
- **Date:** 2026-07-14

## Solution

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def getPos(num):
            r = (num - 1) // n
            c = (num - 1) % n

            if r % 2 == 1:
                c = n - 1 - c

            r = n - 1 - r
            return r, c

        q = deque([(1, 0)])
        visited = {1}

        while q:
            square, moves = q.popleft()

            if square == n * n:
                return moves

            for dice in range(1, 7):
                nxt = square + dice

                if nxt > n * n:
                    break

                r, c = getPos(nxt)

                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))

        return -1
```

---
*Generated automatically by LeetFeedback Extension*
