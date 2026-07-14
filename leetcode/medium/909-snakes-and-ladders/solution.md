# Snakes and Ladders

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/snakes-and-ladders/submissions/2067714590/
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

            return (r,c)

        q = deque()
        q.append((1, 0))
        visited = set()
        visited.add(1)

        while q:
            curr, moves = q.popleft()

            if curr == n * n: return moves

            for dice in range(1, 7):
                next = curr + dice

                if next > n * n: break

                r,c = getPos(next)

                if board[r][c] != -1:
                    next = board[r][c]

                if next in visited: continue

                q.append((next, moves + 1))
                visited.add(next)
            

        return -1


        



        
```

---
*Generated automatically by LeetFeedback Extension*
