# Word Search

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/word-search/submissions/1954051147/
- **Date:** 2026-03-20

## Solution

```python
class Solution:
    def func(self, board, i, j, word, k):
        if k == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = ' '

        ans = (self.func(board, i + 1, j, word, k + 1) or
               self.func(board, i - 1, j, word, k + 1) or
               self.func(board, i, j + 1, word, k + 1) or
               self.func(board, i, j - 1, word, k + 1))

        board[i][j] = temp
        
        return ans

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.func(board, i, j, word, 0):
                        return True
        return False

```

---
*Generated automatically by LeetFeedback Extension*
